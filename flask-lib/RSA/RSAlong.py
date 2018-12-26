# -*- coding:utf-8 -*-

import base64
import json

from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA


class Crypt:
    private_key_filepath = ""
    public_key_filepath = ""

    def __init__(self, private_key_filepath, public_key_filepath):
        self.private_key_filepath = private_key_filepath
        self.public_key_filepath = public_key_filepath

    # 建钥匙
    def rsa_creatkey(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        file_out = open(self.private_key_filepath, "wb")
        file_out.write(private_key)

        public_key = key.publickey().export_key()
        file_out = open(self.public_key_filepath, "wb")
        file_out.write(public_key)

    def rsa_long_encrypt(self, msg):
        '''
        单次加密串的长度最大为(key_size/8 - 11)
        加密的 plaintext 最大长度是 证书key位数/8 - 11, 例如1024 bit的证书，被加密的串最长 1024/8 - 11=117,
        解决办法是 分块 加密，然后分块解密就行了，
        因为 证书key固定的情况下，加密出来的串长度是固定的。
        '''
        length = len(msg)
        default_length = 245
        # 公钥加密
        keyobj = RSA.importKey(open(self.public_key_filepath).read())
        pubobj = Cipher_pkcs1_v1_5.new(keyobj)
        # 长度不用分段
        if length < default_length:
            return base64.b64encode(pubobj.encrypt(msg))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(pubobj.encrypt(msg[offset:offset + default_length]))
            else:
                res.append(pubobj.encrypt(msg[offset:]))
            offset += default_length
        byte_data = b''.join(res)

        return base64.b64encode(byte_data)

    def rsa_long_decrypt(self, msg):
        msg = base64.b64decode(msg)
        length = len(msg)
        default_length = 256
        # 私钥解密
        keyobj = RSA.importKey(open(self.private_key_filepath).read())
        priobj = Cipher_pkcs1_v1_5.new(keyobj)
        # 长度不用分段
        if length < default_length:
            return b''.join(priobj.decrypt(msg, b'fail to decrypt'))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(priobj.decrypt(msg[offset:offset + default_length], b'fail to decrypt'))
            else:
                res.append(priobj.decrypt(msg[offset:], b'fail to decrypt'))
            offset += default_length

        return b''.join(res)


if __name__ == '__main__':
    crypt = Crypt("private_key.pem", "public_key.pem")
    msg = json.dumps({'基本信息查询':{'姓名': '陈怡海', '银行卡': '6222081001025124961', '身份证': '310109198210181535', '手机号': '13917880205', '手机号码运营商': '移动', '手机号码在网状态': '在网', '手机号码在网时长': '24个月以上'}, '直系联系人紧急联系人是否命中': {'银行短时逾期': '否', '银行小额逾期': '否', '银行中额逾期': '否', '银行大额逾期': '否', '银行信用不良': '否', '银行失联': '否', '小贷逾期': '否', '小贷信用不良': '否', '小贷失联': '否', 'P2P逾期': '否', 'P2P信用不良': '否', 'P2P失联': '否', '非银其他机构逾期': '否', '非银其他机构信用不良': '否', '非银其他机构失联': '否', '消费金融逾期': '否', '消费金融信用不良': '否', '银行/小贷/P2P等丧失还款能力': '否'}, '其他不良风险是否命中': {'商业保险信用不良风险': '否', '商业保险大额逾期风险': '否', '商业保险频繁逾期风险': '否', '银行诈骗风险': '否', 'P2P诈骗风险': '否', '消费金融诈骗风险': '否', '银行虚假申请风险': '否', 'P2P虚假申请风险': '否', '消费金融虚假申请风险': '否', '银行虚假资料风险': '否', 'P2P虚假资料风险': '否', '消费金融虚假资料风险': '否', '银行伪冒他人风险': '否', '商业保险伪冒他人风险': '否', '银行疑似欺诈风险': '否', 'P2P疑似欺诈风险': '否', '消费金融疑似欺诈风险': '否', '消费金融失联风险': '否'}, '命中法院个人失信': {}}).encode()
    crypt.rsa_creatkey()
    encrypttext = crypt.rsa_long_encrypt(msg)
    print(encrypttext.decode())
    decrypttext = crypt.rsa_long_decrypt(encrypttext)
    print(json.loads(decrypttext))
    print("分段加解密成功") if msg == decrypttext else print("分段加解密失败")

