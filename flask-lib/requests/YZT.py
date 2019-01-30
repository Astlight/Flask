# -*- coding:utf-8 -*-
import requests

dev_host_url = "https://sandbox.99bill.com/finder"
pro_host_url = "https://sandbox.99bill.com/finder "
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    "Content-Length": "99",
    "Content-Typ": "application/json",
    "charset": "UTF-8",
    "X-99Bill-TraceId": "TBD",  # 请求跟踪号 AN64 调用方保证不要重复，蝶巢在响应中也会通 过HTTP Header返回对应请求的跟踪号。
    "X-99Bill-PlatformCode": "TBD",  # 商户平台代码 N15 蝶巢分配给商户平台的15位会员号
    "X-99Bill-Signature": "TBD",  # 消息签名 AN1024 使用商户平台的私钥对HTTP Body 中的内 容进行签名， 盈账通平台用商户的公钥进行 验签
}

# 公共响应码
YZT_public_response_code = {
    "0000": "成功",
    "1001": "参数校验错误",
    "9997": "业务处理失败",
    "9998": "调用后端业务系统失败",
    "9999": "系统异常",
}
# 证件类型
idCardType = {
    "101": "身份证",
    "102": "护照",
    "103": "军官证",
    "104": "士兵证",
    "105": "港澳台通行证",
    "106": "临时身份证",
    "107": "户口本",
    "108": "警官证",
    "109": "外国人居留证",
    "110": "回乡证",
    "111": "台胞证",
    "112": "其他类型证件",
    "113": "外国护照",
}
# 企业证件类型
enterpriseIdCardType = {
    "201": "营业执照",
    "202": "组织机构代码证",
}
# 路由编号
routeId = {
    "AIB011001": "百信银行",
    "HXB21001": "华夏银行",
    "ONEB035001": "华通银行",

}
# 账户余额类型
accountBalanceType = {
    "SPAD0001": "待分账账户",
    "SPAW0001": "可提现账户",
}
# 文件类型
fileType = {
    "01": "身份证正面",
    "02": "身份证反面",
    "03": "企业三证合一或营业执照",
}
# 职业类型
occupationType = {
    "1A": "各类专业、技术人员",
    "1B": "国家机关、党群组织、企事业单位的负责人",
    "1C": "办事人员和有关人员",
    "1D": "商务工作人员",
    "1E": "服务性工作人员",
    "1F": "农林牧渔劳动者",
    "1G": "生产工作、运输工作和部分体力劳动者",
    "1H": "不便分类的其他劳动者",
}
# 审核状态
auditStatus = {
    "01": "待审核",
    "02": "待复核",
    "03": "审核通过",
    "04": "审核不通过",
}


# 平台
class Enterprise:
    # 子平台开户 /enterprise/addSub
    def enterpriseAddSub(self):
        url = "/enterprise/addSub"
        uId = "uId"  # 平台用户 id
        parentPlatformCode = "parentPlatformCode"  # 上一级平台代码
        name = "name"  # 客户名称
        mobile = "mobile"  # 手机
        email = "email"  # 企业注册邮箱
        idCardType = "idCardType"  # 证件类型
        idCardNumber = "idCardNumber"  # 证件号码
        address = "address"  # 经营地址
        registDate = "registDate"  # 成立日期 20180101
        legalName = "legalName"  # 法人姓名
        legalId = "legalId"  # 法人身份证号码
        legalPhone = "legalPhone"  # 法人手机号
        contactName = "contactName"  # 联系人
        contactPhone = "contactPhone"  # 联系电话
        contactAddr = "contactAddr"  # 联系地址
        request_data = {"uId": uId,
                        "parentPlatformCode": parentPlatformCode,
                        "name": name,
                        "mobile": mobile,
                        "email": email,
                        "idCardType": idCardType,
                        "idCardNumber": idCardNumber,
                        "address": address,
                        "registDate": registDate,
                        "legalName": legalName,
                        "legalId": legalId,
                        "legalPhone": legalPhone,
                        "contactName": contactName,
                        "contactPhone": contactPhone,
                        "contactAddr": contactAddr,
                        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            platformCode = response_data.get("platformCode")  # 子平台代码
            keepingAccounts = response_data.get("keepingAccounts")  # 银行记账号
            return platformCode, keepingAccounts
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 子平台信息变更 /enterprise/updateSub
    def enterpriseUpdateSub(self):
        url = "/enterprise/updateSub"
        uId = "uId"  # 平台用户 id
        parentPlatformCode = "parentPlatformCode"  # 上一级平台代码
        name = "name"  # 客户名称
        mobile = "mobile"  # 手机
        email = "email"  # 企业注册邮箱
        idCardType = "idCardType"  # 证件类型
        idCardNumber = "idCardNumber"  # 证件号码
        legalName = "legalName"  # 法人姓名
        contactName = "contactName"  # 联系人
        contactPhone = "contactPhone"  # 联系电话
        contactAddr = "contactAddr"  # 联系地址
        request_data = {"uId": uId,
                        "parentPlatformCode": parentPlatformCode,
                        "name": name,
                        "mobile": mobile,
                        "email": email,
                        "idCardType": idCardType,
                        "idCardNumber": idCardNumber,
                        "legalName": legalName,
                        "contactName": contactName,
                        "contactPhone": contactPhone,
                        "contactAddr": contactAddr,
                        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            return response_data
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg


# 商户会员
class Merchant:
    # 子商户开户（修改）/merchant/register
    def register(self):
        url = "/merchant/register"
        uId = "uId"  # 平台用户 id
        parentPlatformCode = "parentPlatformCode"  # 上一级平台代码
        name = "name"  # 客户名称
        mobile = "mobile"  # 手机
        email = "email"  # 企业注册邮箱
        idCardType = "idCardType"  # 证件类型
        idCardNumber = "idCardNumber"  # 证件号码
        address = "address"  # 经营地址
        registDate = "registDate"  # 成立日期 20180101
        legalName = "legalName"  # 法人姓名
        legalId = "legalId"  # 法人身份证号码
        legalPhone = "legalPhone"  # 法人手机号
        contactName = "contactName"  # 联系人
        contactPhone = "contactPhone"  # 联系电话
        contactAddr = "contactAddr"  # 联系地址
        accessoryFile = "accessoryFile"  # 证件照片附件
        request_data = {"uId": uId,
                        "parentPlatformCode": parentPlatformCode,
                        "name": name,
                        "mobile": mobile,
                        "email": email,
                        "idCardType": idCardType,
                        "idCardNumber": idCardNumber,
                        "address": address,
                        "registDate": registDate,
                        "legalName": legalName,
                        "legalId": legalId,
                        "legalPhone": legalPhone,
                        "contactName": contactName,
                        "contactPhone": contactPhone,
                        "contactAddr": contactAddr,
                        "accessoryFile": accessoryFile,
                        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            openId = response_data.get("openId")  # 蝶巢侧用户 id
            memberBankAcctId = response_data.get("memberBankAcctId")  # 银行卡主键Id信息 O
            auditStatus = response_data.get("auditStatus")  # 审核状态
            return openId, memberBankAcctId, auditStatus
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 子商户开户+绑卡 /merchant/registerAndBindCard
    def registerAndBindCard(self):
        url = "/merchant/registerAndBindCard"
        uId = "uId"  # 平台用户 id
        parentPlatformCode = "parentPlatformCode"  # 上一级平台代码 O
        name = "name"  # 客户名称
        mobile = "mobile"  # 手机
        email = "email"  # 企业注册邮箱
        idCardType = "idCardType"  # 证件类型
        idCardNumber = "idCardNumber"  # 证件号码
        address = "address"  # 经营地址
        registDate = "registDate"  # 成立日期
        legalName = "legalName"  # 法人姓名
        legalId = "legalId"  # 法人身份证号码
        legalPhone = "legalPhone"  # 法人手机号
        repIssDate = "repIssDate"  # 法人证件签发日期
        contactName = "contactName"  # 联系人
        contactPhone = "contactPhone"  # 联系电话
        contactAddr = "contactAddr"  # 联系地址
        bankId = "bankId"  # 银行编号
        bankAcctId = "bankAcctId"  # 银行卡号
        bankAcctName = "bankAcctName"  # 绑定账户名称
        bankName = "bankName"  # 开户行名称
        bankProvince = "bankProvince"  # 开户行省份
        bankCity = "bankCity"  # 开户行城市
        accountType = "accountType"  # # 账户类型 ,默认值：0 >>> 0:出入金，1:白名单1，2:白名单2，3:白名单3
        bankAcctType = "bankAcctType"  # 对公和对私,默认值：1 >>> 1:公司, 2:个人
        accountSign = "accountSign"  # 卡号/账号标识，默认值：0 >>> 0:卡号, 1:账号
        secondAcct = "secondAcct"  # 二类账户, 默认为：0 >>> 0:否,1:是
        industryType = "industryType"  # 行业代码
        industry = "industry"  # 通用行业代码
        state = "state"  # 省、州
        city = "city"  # 城市
        scale = "scale"  # 企业规模, 01：大型, 02：中型, 03：小型, 04：微型,98：其他
        authCapital = "authCapital"  # 注册资本
        socialCreditCode = "socialCreditCode"  # 统一社会信息证代码
        licenceExpiryDate = "licenceExpiryDate"  # 统一社会信息证有效期.如证件未记录有效期则设定为 21000101，当证件长期有效时为 99991231
        accessoryFile = "accessoryFile"  # 证件照片附件
        request_data = {"uId": uId,
                        "parentPlatformCode": parentPlatformCode,
                        "name": name,
                        "mobile": mobile,
                        "email": email,
                        "idCardType": idCardType,
                        "idCardNumber": idCardNumber,
                        "address": address,
                        "registDate": registDate,
                        "legalName": legalName,
                        "legalId": legalId,
                        "legalPhone": legalPhone,
                        "contactName": contactName,
                        "contactPhone": contactPhone,
                        "contactAddr": contactAddr,
                        "accessoryFile": accessoryFile,
                        "repIssDate": repIssDate,
                        "bankId": bankId,
                        "bankAcctId": bankAcctId,
                        "bankAcctName": bankAcctName,
                        "bankName": bankName,
                        "bankProvince": bankProvince,
                        "bankCity": bankCity,
                        "accountType": accountType,
                        "bankAcctType": bankAcctType,
                        "accountSign": accountSign,
                        "secondAcct": secondAcct,
                        "industryType": industryType,
                        "industry": industry,
                        "state": state,
                        "city": city,
                        "scale": scale,
                        "authCapital": authCapital,
                        "socialCreditCode": socialCreditCode,
                        "licenceExpiryDate": licenceExpiryDate,
                        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            openId = response_data.get("openId")  # 蝶巢侧用户 id
            memberBankAcctId = response_data.get("memberBankAcctId")  # 银行卡主键Id信息
            return openId, memberBankAcctId

        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 子商户信息变更 /merchant/updateMember
    def updateMember(self):
        url = "/merchant/updateMember"
        uId = "uId"
        platformCode = "platformCode"
        mobile = "mobile"
        legalName = "legalName"
        contactName = "contactName"
        contactPhone = "contactPhone"
        contactAddr = "contactAddr"
        request_data = {"uId": uId,
                        "platformCode": platformCode,
                        "mobile": mobile,
                        "legalName": legalName,
                        "contactName": contactName,
                        "contactPhone": contactPhone,
                        "contactAddr": contactAddr,
                        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 查询会员信息（修改） /merchant/info
    def info(self):
        url = "/merchant/info"
        uId = "uId"
        platformCode = "platformCode"
        request_data = {"uId": uId,
                        "platformCode": platformCode,
                        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            idCardType = response_data.get("idCardType")
            idCardNumber = response_data.get("idCardNumber")
            name = response_data.get("name")
            mobile = response_data.get("mobile")
            email = response_data.get("email")
            address = response_data.get("address")
            legalName = response_data.get("legalName")
            legalId = response_data.get("legalId")
            legalPhone = response_data.get("legalPhone")
            registDate = response_data.get("registDate")
            contactName = response_data.get("contactName")
            contactPhone = response_data.get("contactPhone")
            contactAddr = response_data.get("contactAddr")
            status = response_data.get("status")
            auditStatus = response_data.get("auditStatus")
            return response_data
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 提现绑定银行卡 /merchant/bankcard/bind
    def bankcardBind(self):
        url = "/merchant/bankcard/bind"
        uId = "uId"  # 平台用户 id
        platformCode = "platformCode"  # 商户平台代码
        bankId = "bankId"  # 银行编号
        bankAcctId = "bankAcctId"  # 银行卡号
        name = "name"  # 户名
        mobile = "mobile"  # 银行预留手机号
        bankName = "bankName"  # 开户行名称
        province = "bankProvince"  # 开户行省份
        city = "bankCity"  # 开户行城市
        accountType = "accountType"  # 账户类型 ,默认值：0 >>> 0:出入金，1:白名单1，2:白名单2，3:白名单3
        bankType = "bankType"  # 对公和对私 默认值：1 >>> 1:公司, 2:个人
        accountSign = "accountSign"  # 卡号/账号标识 默认值：1 >>> 0:卡号 1:账号
        idCardType = "idCardType"  # 证件类型
        idCardNumber = "idCardNumber"  # 证件号码 当出入金账户为对公账户时填企业证件号码，当出入金账户为个人账户时，填身份证号
        request_data = {
            "uId": uId,
            "platformCode": platformCode,
            "bankId": bankId,
            "bankAcctId": bankAcctId,
            "name": name,
            "mobile": mobile,
            "bankName": bankName,
            "province": province,
            "city": city,
            "accountType": accountType,
            "bankType": bankType,
            "accountSign": accountSign,
            "idCardType": idCardType,
            "idCardNumber": idCardNumber,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            memberBankAcctId = response_data.get("memberBankAcctId")  # 银行卡主键Id信息
            return memberBankAcctId
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 变更提现绑定银行卡 /merchant/bankcard/rebind
    def bankcardRebind(self):
        url = "/merchant/bankcard/rebind"
        uId = "uId"  # 平台用户 id
        platformCode = "platformCode"  # 商户平台代码
        bankId = "bankId"  # 银行编号
        bankAcctId = "bankAcctId"  # 银行卡号
        name = "name"  # 户名
        mobile = "mobile"  # 银行预留手机号
        bankName = "bankName"  # 开户行名称
        province = "bankProvince"  # 开户行省份
        city = "bankCity"  # 开户行城市
        accountType = "accountType"  # 账户类型 ,默认值：0 >>> 0:出入金，1:白名单1，2:白名单2，3:白名单3
        bankType = "bankType"  # 对公和对私 默认值：1 >>> 1:公司, 2:个人
        accountSign = "accountSign"  # 卡号/账号标识 默认值：1 >>> 0:卡号 1:账号
        idCardType = "idCardType"  # 证件类型
        idCardNumber = "idCardNumber"  # 证件号码 当出入金账户为对公账户时填企业证件号码，当出入金账户为个人账户时，填身份证号
        request_data = {
            "uId": uId,
            "platformCode": platformCode,
            "bankId": bankId,
            "bankAcctId": bankAcctId,
            "name": name,
            "mobile": mobile,
            "bankName": bankName,
            "province": province,
            "city": city,
            "accountType": accountType,
            "bankType": bankType,
            "accountSign": accountSign,
            "idCardType": idCardType,
            "idCardNumber": idCardNumber,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            memberBankAcctId = response_data.get("memberBankAcctId")  # 银行卡主键Id信息
            return memberBankAcctId
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 注销提现绑定银行卡 /merchant/bankcard/cance
    def bankcardCancel(self):
        url = "/merchant/bankcard/cance"
        uId = "uId"  # 平台用户 id
        platformCode = "platformCode"  # 商户平台代码
        accountType = "accountType"  # 账户类型 ,默认值：0 >>> 0:出入金，1:白名单1，2:白名单2，3:白名单3
        request_data = {
            "uId": uId,
            "platformCode": platformCode,
            "accountType": accountType,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            return response_data
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 查询银行卡列表 /merchant/bankcard/list
    def bankcardList(self):
        url = "/merchant/bankcard/list"
        uId = "uId"  # 平台用户 id
        platformCode = "platformCode"  # 商户平台代码
        request_data = {
            "uId": uId,
            "platformCode": platformCode,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            bindCardList = response_data.get("response_data")
            return bindCardList
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg


# 银行卡
class Bankacct:
    # 查询提现绑卡状态 /bankacct/queryStatus
    def bankacctQueryStatus(self):
        url = "/bankacct/queryStatus"
        uId = "uId"  # 平台用户 id
        platformCode = "platformCode"  # 商户平台代码
        bankAcctId = "bankAcctId"  # 银行卡号/结算账号
        request_data = {
            "uId": uId,
            "platformCode": platformCode,
            "bankAcctId": bankAcctId,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            bindCardList = response_data.get("response_data")
            return bindCardList
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg


# 账户
class Account:
    # 账户余额查询 /account/balance/query
    def accountBlanceQuery(self):
        url = "/account/balance/query"
        uId = "uId"  # 平台用户 id
        platformCode = "platformCode"  # 商户平台代码
        accountBalanceType = "accountBalanceType"  # 账户余额类型数组 >>> SPAD0001:待分账账户,SPAW0001:可提现账户
        request_data = {
            "uId": uId,
            "platformCode": platformCode,
            "accountBalanceType": accountBalanceType,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            accountBalanceList = response_data.get("accountBalanceList")
            return accountBalanceList
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 提现 /account/withdraw
    def accountWithdraw(self):
        url = "/account/withdraw"
        outTradeNo = "outTradeNo"  # 外部交易号,platformCode+outTradeNo 保证唯一
        uId = "uId"  # 平台用户 id
        platformCode = "platformCode"  # 商户平台代码
        amount = "amount"  # 提现金额
        bgUrl = "bgUrl"  # 通知地址
        customerFee = "customerFee"  # 会员自付手续费,如果没有，填 0
        merchantFee = "merchantFee"  # 商户代付手续费,如果没有，填 0
        memo = "memo"  # 交易摘要,默认 withdraw
        memberBankAcctId = "memberBankAcctId"  # 银行卡主键 Id 信息
        bankAcctId = "bankAcctId"  # 银行账号
        # memberBankAcctId,bankAcctId都不传，默认取已绑定的提现主卡。传了优先取 bankAcctId，bankAcctId 为空的时候再取 memberBankAcctId
        request_data = {
            "outTradeNo": outTradeNo,
            "uId": uId,
            "platformCode": platformCode,
            "amount": amount,
            "bgUrl": bgUrl,
            "customerFee": customerFee,
            "merchantFee": merchantFee,
            "memo": memo,
            "memberBankAcctId": memberBankAcctId,
            "bankAcctId": bankAcctId,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            dealId = response_data.get("dealId")  # 盈账通内部交易编号
            status = response_data.get("status")  # 订单状态 >>> 1:成功，2:失败，3:处理中
            return dealId, status
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 提现明细查询 /withdraw/query
    def withdrawQuery(self):
        url = "/withdraw/query"
        outTradeNo = "outTradeNo"
        uId = "uId"  # 平台用户 id
        platformCode = "platformCode"  # 商户平台代码
        request_data = {
            "outTradeNo": outTradeNo,
            "uId": uId,
            "platformCode": platformCode,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            outTradeNo = response_data.get("outTradeNo")  # 外部交易号
            amount = response_data.get("amount")  # 提现金额
            customerFee = response_data.get("customerFee")  # 会员自付手续费
            merchantFee = response_data.get("merchantFee")  # 商户代付手续费
            memberBankAcctId = response_data.get("memberBankAcctId")  # 银行卡主键 id
            bankAcctId = response_data.get("bankAcctId")  # 银行账户
            bgUrl = response_data.get("bgUrl")  # 通知地址
            memo = response_data.get("memo")  # 交易摘要
            status = response_data.get("status")  # 订单状态 >>> 1:成功，2:失败，3:处理中
            tradeDescription = response_data.get("tradeDescription")  # 订单交易描述 >>>成功，处理中，或者为失败原因
            return response_data
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 提现手续费查询 /withdraw/queryFee
    def withdrawQueryFee(self):
        url = "/withdraw/queryFee"
        uId = "uId"  # 平台用户 id
        platformCode = "platformCode"  # 商户平台代码
        amount = "amount"  # 提现金额
        request_data = {
            "uId": uId,
            "platformCode": platformCode,
            "amount": amount,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            fee = response_data.get("fee")  # 手续费
            return fee
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg


# 分账
class settle:
    # 消费分账 /settle/pay
    def settlePay(self):
        url = "/settle/pay"
        settleUid = "settleUid"  # 分账平台外部编号,子平台分账时传子平台的外部编号,不传表示由平台分账（取 HTTP Header 里的X-99Bill-PlatformCode）
        outTradeNo = "outTradeNo"  # 外部订单号
        totalAmount = "totalAmount"  # 分账总金额
        feeMode = "feeMode"  # 手续费收取方式,, 默认 0 >>> 0:主收款方方式 1:均摊方式
        feePayerUid = "feePayerUid"  # 手续费主收款方外部编号,feeMode=0 时且由子商户或子平台支付手续费的情况下需要。不传表示从接入平台收取
        settleData = "settleData"  # 分账数据,参见数据元 SettleData 定义。同一订单有 n 个分账方，针对此订单会产生 n条分账数据。
        notifyUrl = "notifyUrl"  # 分账结果通知URL,结果回调地址
        orderDetails = "orderDetails"  # 订单数据 订单数据， 参见 OrderDetail 定义
        request_data = {
            "settleUid": settleUid,
            "outTradeNo": outTradeNo,
            "totalAmount": totalAmount,
            "feeMode": feeMode,
            "feePayerUid": feePayerUid,
            "settleData": settleData,
            "notifyUrl": notifyUrl,
            "orderDetails": orderDetails,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            return response_data
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 退货分账 /settle/refund
    def settleRefund(self):
        url = "/settle/refund"
        outTradeNo = "outTradeNo"  # 外部订单号
        origOutOrderNo = "origOutOrderNo"  # 原始交易号, 退货对应的正向交易号
        totalAmount = "totalAmount"  # 分账总金额
        settleData = "settleData"  # 分账数据,参见数据元 SettleData 定义。同一订单有 n 个分账方，针对此订单会产生 n条分账数据。
        notifyUrl = "notifyUrl"  # 分账结果通知URL,结果回调地址
        request_data = {
            "outTradeNo": outTradeNo,
            "origOutOrderNo": origOutOrderNo,
            "totalAmount": totalAmount,
            "settleData": settleData,
            "notifyUrl": notifyUrl,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            return response_data
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 结算周期修改 /settle/period/modify
    def settlePeriodModify(self):
        url = "/settle/period/modify"
        outTradeNo = "outTradeNo"  # 外部订单号
        origOutOrderNo = "origOutOrderNo"  # 原始交易号, 退货对应的正向交易号
        settlePeriod = "settlePeriod"  # 结算周期
        request_data = {
            "outTradeNo": outTradeNo,
            "origOutOrderNo": origOutOrderNo,
            "settlePeriod": settlePeriod,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            return response_data
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg

    # 分账结果查询 /settle/detail
    def settleDetail(self):
        url = "/settle/detail"
        outTradeNo = "outTradeNo"  # 外部订单号
        origOutOrderNo = "origOutOrderNo"  # 原始交易号, 退货对应的正向交易号
        request_data = {
            "outTradeNo": outTradeNo,
            "origOutOrderNo": origOutOrderNo,
        }
        response = requests.post(dev_host_url + url, headers=headers, json=request_data, timeout=(7, None))
        if response.status_code == "0000":
            response_data = response.json()
            settleUid = response_data.get("settleUid")  # 分账平台外部编号 ,子平台分账时有值
            settlePlatformCode = response_data.get(
                "settlePlatformCode")  # 分账平台编号,平台分账时有值（和分账请求中的X-99Bill-PlatformCode 相等）
            outOrderNo = response_data.get("outOrderNo")  # 外部交易号,正向交易或退货交易单号
            origOutOrderNo = response_data.get("origOutOrderNo")  # 原始交易号,查询退货时为正向交易单号
            txnType = response_data.get("txnType")  # 交易类型,1:消费，2:退货
            feeMode = response_data.get("feeMode")  # 手续费收取方式,默认 0 >>> 0:主收款方方式 1:均摊方式,
            feePayerUid = response_data.get("feePayerUid")  # 手续费主收款方外部编号, feeMode=0 时且由子商户或子平台支付手续费的情况下
            feePayerPlatformCode = response_data.get("feePayerPlatformCode")  # 手续费主收款方平台编号, feeMode=0 时且由平台支付手续费的情况下有值
            totalAmount = response_data.get("totalAmount")  # 分账总金额
            fee = response_data.get("fee")  # 分账手续费
            settleResult = response_data.get("settleResult")  # 分账结果明细,请求参数中 outSubOrderNo 为空的情况下返回全部数据， 否则只返回满足条件的明细
            return response_data
        else:
            response_data = response.json()
            rspCode = response_data.get("rspCode")
            rspMsg = response_data.get("rspMsg ")
            return rspCode, rspMsg
