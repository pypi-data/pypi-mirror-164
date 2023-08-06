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
import shutil
import yaml
from pathlib import Path
from helper import (
            connect_to_prototyping_board, generate_custom_pki,
            verify_cert_chain, verify_SE_with_random_challenge,
            generate_verify_cert, upload_device_quarklink,
            upload_certificate_quarklink, generate_project_config_h)
from tpds.tp_utils.tp_print import print
from tpds.tp_utils.tp_settings import TPSettings


class QuarklinkConnectUsecase():
    def __init__(self, boards):
        self.boards = boards
        self.default_creds = {
            'title': 'Quarklink IoT Credentials',
            'user_name': '',
            'password': '',
            'url': ''
        }
        self.creds_file = os.path.join(
                            TPSettings().get_base_folder(),
                            'quarklink_credentials.yaml')
        if not os.path.exists(self.creds_file):
            Path(self.creds_file).write_text(
                    yaml.dump(self.default_creds, sort_keys=False))

    def generate_resources(self, b=None):
        element = connect_to_prototyping_board(self.boards, b)
        assert element, 'Connection to Board failed'

        print('Generating Custom PKI certificates...', canvas=b)
        generate_custom_pki(b)
        self.root_crt = 'root_crt.crt'
        self.root_cer = 'root_crt.cer'
        self.root_key = 'root_key.key'
        self.signer_crt = 'signer_FFFF.crt'
        self.signer_key = 'signer_FFFF.key'
        self.cust_def_1_c = 'cust_def_1_signer.c'
        self.cust_def_1_h = 'cust_def_1_signer.h'
        self.cust_def_2_c = 'cust_def_2_device.c'
        self.cust_def_2_h = 'cust_def_2_device.h'
        serial_number = element.get_device_serial_number().hex().upper()
        self.device_crt = f'device_{serial_number}.crt'
        shutil.copyfile(self.root_crt, self.root_cer)
        generate_project_config_h(cert_type='Custom', address=0x6C)

    def register_root(self, b=None):
        # Register signer
        print('Generating Verification Root Certificate for connecting to Quarklink ...', canvas=b)
        generate_verify_cert(b)

    def register_certificate(self, b=None):
        # Register certificate
        print('Registering Signer Certificate to Quarklink...')
        with open(self.creds_file) as f:
            quarklink_credentials = yaml.safe_load(f)
        if all(dict((k, v.strip()) for k, v in quarklink_credentials.items()).values()):
            OEMRoot = upload_certificate_quarklink('Default', quarklink_credentials)
            if OEMRoot is not None:
                with open('ql_connect.h', 'w') as f:
                    f.write('#ifndef _QUARKLINK_CONNECT_H\n')
                    f.write('#define _QUARKLINK_CONNECT_H\n\n')
                    f.write('#include "cryptoauthlib.h"\n\n')
                    f.write('#ifdef __cplusplus\n')
                    f.write('extern "C" {\n')
                    f.write('#endif\n\n')
                    f.write(f'''#define QUARKLINK_URL "{quarklink_credentials.get('url')}"\n\n''')
                    # f.write(f'''#define OEMRoot "{OEMRoot}"\n\n''')
                    f.write('#ifdef __cplusplus\n')
                    f.write('}\n')
                    f.write('#endif\n')
                    f.write('#endif\n')
            else:
                print('Error occurred while fetching OEMRoot')
        else:
            raise ValueError('Invalid Quarklink Credentials...')

    def register_device(self, b=None):
        # Register Device
        device_id = 'CQ-'+self.device_crt.split('.')[0].split('_')[1]
        print(f'Registering device {device_id} to Quarklink...')
        upload_device_quarklink(self.creds_file, device_id, 'Default')

    def verify_cert_chain(self, b=None):
        device_cert, crt_template = verify_cert_chain(
                    self.root_crt, self.root_key,
                    self.signer_crt, self.signer_key,
                    self.device_crt, b)
        self.device_crt = device_cert
        self.crt_template = crt_template

    def verify_SE_with_random_challenge(self, b=None):
        verify_SE_with_random_challenge(
                    self.device_crt, self.crt_template['device'], b)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    pass
