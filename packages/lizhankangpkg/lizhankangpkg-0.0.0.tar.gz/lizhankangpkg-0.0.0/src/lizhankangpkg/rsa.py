# coding:utf-8 
# @Author : lizhankang
# @Subject : 
# @Time : 2023 - 11 - 09
import base64
import json
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

def signer(data_dict, rsa_key_path = ""):
    """
    加签
    :param data_dict: 待签名dict对象
    :param rsa_key_path: 密钥路径
    :return: 签名(str)
    """
    if rsa_key_path == "":
        print("请输入密钥路径")
        return
    with open(rsa_key_path, mode='rb') as f:
        rsa_private_key = RSA.import_key(f.read())
    # PKCS1_v1_5类型的签名方式
    secret_key_obj = PKCS1_v1_5.new(rsa_private_key)
    request_hash = SHA256.new(json.dumps(data_dict, separators=(',', ':'), ensure_ascii=False).encode('utf-8'))
    # 计算signature
    signature_byte = secret_key_obj.sign(request_hash)
    return base64.b64encode(signature_byte).decode('utf-8')
