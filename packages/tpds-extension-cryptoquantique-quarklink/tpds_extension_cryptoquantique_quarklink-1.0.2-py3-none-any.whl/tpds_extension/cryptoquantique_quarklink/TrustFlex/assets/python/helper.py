# -*- coding: utf-8 -*-
# 2018 to present - Copyright Microchip Technology Inc. and its subsidiaries.
# Copyright (c) 2021-2022 Crypto Quantique Ltd

# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.

# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR
# PURPOSE. IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL,
# PUNITIVE, INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY
# KIND WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP
# HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.

import os
import subprocess
import json
import cryptoauthlib as cal
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives import hashes
from create_certs_verif import create_iotconnect_root_verify

from tpds.resource_generation import TFLXResources
from tpds.flash_program import FlashProgram
from tpds.secure_element import ECC608A
from tpds.tp_utils.tp_print import print
from tpds.certs.tflex_certs import TFLEXCerts
import tpds.tp_utils.tp_input_dialog as tp_userinput
from tpds.tp_utils.tp_keys import TPAsymmetricKey
from tpds.certs.cert_utils import get_backend
from tpds.tp_utils.tp_settings import TPSettings
from tpds.proto_boards import get_board_path


def connect_to_prototyping_board(board, b):
    assert board is not None, "Prototyping board MUST be selected!"
    assert board.get_selected_board() is not None, 'Select board to run an Usecase!'

    print('Connecting to Secure Element: ', end='')
    print('FW status: ', end='')
    kit_parser = FlashProgram()
    print(kit_parser.check_board_status())
    assert kit_parser.is_board_connected(), \
        'Board not found! Verify I2C switch position and plug USB cable back again.'
    factory_hex = board.get_kit_hex()
    if not kit_parser.is_factory_programmed():
        assert factory_hex, \
            'Factory hex is unavailable to program'
        print('Programming factory hex...', canvas=b)
        tp_settings = TPSettings()
        path = os.path.join(
            tp_settings.get_tpds_core_path(),
            'assets', 'Factory_Program.X',
            factory_hex)
        print(f'Programming {path} file')
        kit_parser.load_hex_image(path)
    element = ECC608A(address=0x6C)
    print('OK')
    print('Device details: {}'.format(element.get_device_details()))
    return element


def generate_custom_pki(b):
    resources = TFLXResources()
    mchp_certs = resources.get_mchp_certs_from_device()
    if mchp_certs:
        print('MCHP Certs are available on device')
        if not resources.get_mchp_backup_certs():
            print('MCHP Certs backup is unavailable... Take backup!')
            resources.backup_mchp_certs(mchp_certs)
    resources.generate_custom_pki('CQ', 'CQID')
    print('', canvas=b)


def upload_device_quarklink(cred_file_path, device_id, batch):
    print('Configuring Quarklink CLI')
    os.environ["QUARKLINK_CONFIG_PATH"] = cred_file_path
    assert os.path.exists('quarklink.exe'), 'Quarklink exe is missing in the working dir'
    try:
        subprocess.run([os.getcwd(), "add", "devices", device_id, "-b", batch])
    except BaseException as e:
        print(f'''Error: "{e}" occurred while running Quarklink CLI''')


def upload_certificate_quarklink(batch, credentials):
    try:
        os.environ["QUARKLINK_USERNAME"] = credentials.get('user_name')
        os.environ["QUARKLINK_PASSWORD"] = credentials.get('password')
        os.environ["QUARKLINK_URL"] = credentials.get('url')
    except BaseException as e:
        assert False, 'Please follow the steps in the usecase help to create credentials'

    quarklink_cli_path = 'quarklink.exe'
    certificate_path = 'signer_FFFF.crt'
    assert os.path.exists(quarklink_cli_path), 'Quarklink exe is missing in the working dir'
    assert os.path.exists(certificate_path), 'Signer cert is missing in the working dir'

    try:
        tp_settings = TPSettings()
        print([quarklink_cli_path, "add", "certificates", "--certfile", certificate_path, "--batchname", batch])
        subprocess.run([quarklink_cli_path, "add", "certificates", "--certfile", certificate_path, "--batchname", batch])
        result = subprocess.run([quarklink_cli_path, "list", "certificates", "-o", "json"], capture_output=True, text=True)
        for cert in json.loads(result.stdout)["results"]:
            if cert["name"] == 'OEMRoot':
                ql_oemroot = cert["certificatePEM"]
                ql_oemroot_path = os.path.join(tp_settings.get_base_folder(),
                        'winc_firmware_upgrade',
                        'firmware',
                        'Tools',
                        'root_certificate_downloader',
                        'binary',
                        'OEMRoot.cer')
                ql_oemroot_crt = x509.load_pem_x509_certificate(bytes(ql_oemroot, 'utf-8'), default_backend())
                ql_oemroot_der = ql_oemroot_crt.public_bytes(serialization.Encoding.DER)
                with open(ql_oemroot_path, 'wb') as fw:
                    fw.write(ql_oemroot_der)
                return ql_oemroot.replace('\n', '\\n')
        return None
    except BaseException as e:
        assert False, f'''Error "{e}" occurred while running Quarklink CLI'''


def generate_verify_cert(b):
    text_box_desc = (
        '''<font color=#0000ff><b>Verification Root Certificate Setup</b></font><br>
        <br>It is required to activate root CA generated during step 1 to allow signed Secure Element to connect to the cloud.<br>
        <br>Please login to your IoTConnect account, upload root CA and copy/paste verification code below.<br>
        <br>Then press OK and finally upload the verification root certificate to your cloud account:<br>
        <font color=#aaaaaa><br>Note: this step only needs to be done once and may be skipped if necessary.</font><br>''')
    verify = tp_userinput.TPInputTextBox(
                                desc=text_box_desc,
                                dialog_title='Quarklink Connect')
    verify.invoke_dialog()
    if (verify.user_text is None) or (len(str(verify.user_text)) == 0):
        print('No Verification Code provided, skipping Verification Root Certificate generation!', canvas=b)
    else:
        print(f'User Verification Code: {verify.user_text}', canvas=b)
        create_iotconnect_root_verify(verify.user_text)
    print('', canvas=b)


def verify_cert_chain(
                    root_crt, root_key,
                    signer_crt, signer_key,
                    device_crt, b):
    custom_certs = TFLEXCerts()
    custom_certs.root.set_certificate(root_crt)
    custom_certs.root.key = TPAsymmetricKey(root_key)
    custom_certs.signer.set_certificate(signer_crt)
    custom_certs.signer.key = TPAsymmetricKey(signer_key)
    custom_certs.device.set_certificate(device_crt)
    crt_template = custom_certs.get_tflex_py_definitions()

    print('Verifying Custom PKI from Secure Element: ', canvas=b)
    signer_cert_der_len = cal.AtcaReference(0)
    assert cal.CertStatus.ATCACERT_E_SUCCESS == cal.atcacert_max_cert_size(
        crt_template['signer'],
        signer_cert_der_len)
    signer_cert_der = bytearray(signer_cert_der_len.value)
    assert cal.CertStatus.ATCACERT_E_SUCCESS == cal.atcacert_read_cert(
        crt_template['signer'],
        custom_certs.root.key.get_public_key().public_bytes(
            format=serialization.PublicFormat.UncompressedPoint,
            encoding=serialization.Encoding.X962)[1:],
        signer_cert_der,
        signer_cert_der_len)
    signer_cert = x509.load_der_x509_certificate(
                                        bytes(signer_cert_der),
                                        get_backend())

    device_cert_der_len = cal.AtcaReference(0)
    assert cal.CertStatus.ATCACERT_E_SUCCESS == cal.atcacert_max_cert_size(
        crt_template['device'],
        device_cert_der_len)
    device_cert_der = bytearray(device_cert_der_len.value)
    assert cal.CertStatus.ATCACERT_E_SUCCESS == cal.atcacert_read_cert(
        crt_template['device'],
        custom_certs.signer.key.get_public_key().public_bytes(
            format=serialization.PublicFormat.UncompressedPoint,
            encoding=serialization.Encoding.X962)[1:],
        device_cert_der,
        device_cert_der_len)
    device_cert = x509.load_der_x509_certificate(
                                        bytes(device_cert_der),
                                        get_backend())
    print('OK')

    print('Certs from Device...')
    dev_certs = TFLEXCerts()
    dev_certs.signer.set_certificate(signer_cert)
    dev_certs.device.set_certificate(device_cert)
    print(dev_certs.signer.get_certificate_in_text())
    print(dev_certs.device.get_certificate_in_text())

    print('Processing Root...', end='', canvas=b)
    is_cert_valid = custom_certs.root.is_signature_valid(
        custom_certs.root.certificate.public_key())
    print('Valid' if is_cert_valid else 'Invalid', canvas=b)

    print('Processing Signer...', end='', canvas=b)
    is_cert_valid = dev_certs.signer.is_signature_valid(
        custom_certs.root.certificate.public_key())
    print('Valid' if is_cert_valid else 'Invalid', canvas=b)

    print('Processing Device...', end='', canvas=b)
    is_cert_valid = dev_certs.device.is_signature_valid(
        dev_certs.signer.certificate.public_key())
    print('Valid' if is_cert_valid else 'Invalid', canvas=b)
    print('', canvas=b)
    return device_cert, crt_template


def verify_SE_with_random_challenge(device_crt, device_crt_template, b):
    print('Sending random challenge...', canvas=b)
    challenge = os.urandom(32)
    print(f'Challenge: {challenge.hex().upper()}')

    print('Reading response from Secure Element...', canvas=b)
    response = bytearray(64)
    assert cal.atcacert_get_response(
        device_crt_template.private_key_slot,
        challenge, response) == cal.CertStatus.ATCACERT_E_SUCCESS
    print(f'Response: {response.hex().upper()}')

    print('Verifying response...', canvas=b)
    r = int.from_bytes(response[0:32], byteorder='big', signed=False)
    s = int.from_bytes(response[32:64], byteorder='big', signed=False)
    sign = utils.encode_dss_signature(r, s)
    try:
        device_crt.public_key().verify(
            sign, challenge, ec.ECDSA(
                utils.Prehashed(hashes.SHA256())))
    except Exception as err:
        raise ValueError(err)
    print('Valid', canvas=b)
    print('', canvas=b)


def generate_project_config_h(cert_type='MCHP', address=0x6C):
    with open('project_config.h', 'w') as f:
        f.write('#ifndef _PROJECT_CONFIG_H\n')
        f.write('#define _PROJECT_CONFIG_H\n\n')

        f.write('#ifdef __cplusplus\n')
        f.write('extern "C" {\n')
        f.write('#endif\n\n')
        if cert_type == 'MCHP':
            f.write('#define CLOUD_CONNECT_WITH_MCHP_CERTS\n')
        else:
            f.write('#define CLOUD_CONNECT_WITH_CUSTOM_CERTS\n')
        f.write(f'#define SECURE_ELEMENT_ADDRESS 0x{address:02X}\n\n')
        f.write('#ifdef __cplusplus\n')
        f.write('}\n')
        f.write('#endif\n')
        f.write('#endif\n')


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    pass
