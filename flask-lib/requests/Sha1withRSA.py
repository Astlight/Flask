# -*- coding:utf-8 -*-
from base64 import b64encode, b64decode

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_v1_5_cipper
from Crypto.Signature import PKCS1_v1_5 as PKCS1_v1_5_sign
from Crypto.Hash import SHA1


class Sha1withRSA:
    def __init__(self, ciper_lib=PKCS1_v1_5_cipper, sign_lib=PKCS1_v1_5_sign, hash_lib=SHA1,
                 pub_file=None, pri_file=None, reversed_size=11):
        self.ciper_lib = ciper_lib
        self.sign_lib = sign_lib
        self.hash_lib = hash_lib
        self.pub_key = RSA.importKey(open(pub_file).read())
        self.pri_key = RSA.importKey(open(pri_file).read())
        self.block_reversed_size = reversed_size

    def get_block_size(self, rsa_key):
        try:
            reserve_size = self.block_reversed_size
            key_size = rsa_key.size_in_bits()
            if (key_size % 8) != 0:
                raise RuntimeError('RSA 密钥长度非法')
            if rsa_key.has_private():
                reserve_size = 0
            bs = int(key_size / 8) - reserve_size
        except Exception as err:
            print('计算加解密数据块大小出错', rsa_key, err)
        return bs

    def block_data(self, data, rsa_key):
        bs = self.get_block_size(rsa_key)
        for i in range(0, len(data), bs):
            yield data[i:i + bs]

    def sign_bytes(self, data):
        signature = ''
        try:
            rsa_key = self.pri_key
            h = self.hash_lib.new(data)
            signature = self.sign_lib.new(rsa_key).sign(h)
        except Exception as err:
            print('RSA签名失败', '', err)
        return signature

    def sign_verify(self, data, sig):
        rsa_key = self.pub_key
        h = self.hash_lib.new(data)
        return self.sign_lib.new(rsa_key).verify(h, sig)


if __name__ == '__main__':
    pub_key = "../public_key.pem"
    pri_key = "../private_key.pem"
    rsa = Sha1withRSA(pub_file=pub_key, pri_file=pri_key)
    signature = b64encode((rsa.sign_bytes(data=b"test"))).decode()
    print(len(signature))
    rv = rsa.sign_verify(b"test", b64decode(signature))
    print(rv)
