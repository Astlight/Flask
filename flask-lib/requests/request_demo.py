# -*- coding:utf-8 -*-
import requests


kw = {"demo": "demo"}

dev_url = "： https://sandbox.99bill.com/finder"
cookies = dict(cookies_are='working')
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    "Content-Length": "99",
    "Content-Typ": "application/json",
    "charset": "UTF-8",
    "X-99Bill-TraceId": "TBD",  # 请求跟踪号 AN64 调用方保证不要重复，蝶巢在响应中也会通 过HTTP Header返回对应请求的跟踪号。
    "X-99Bill-PlatformCode": "TBD",  # 商户平台代码 N15 蝶巢分配给商户平台的15位会员号
    "X-99Bill-Signature": "TBD",  # 消息签名 AN1024 使用商户平台的私钥对HTTP Body 中的内 容进行签名， 盈账通平台用商户的公钥进行 验签
}
response_post = requests.post(dev_url, headers=headers, json=kw, cookies=cookies, timeout=(7, None))

response_post.text  # 根据HTTP 头部对响应的编码作出有根据的推测，推测的文本编码
response_post.encoding = "gbk"  # 修改编码方式

response_post.content  # bytes
response_post.content.deocde("utf8")  # 修改编码方式

response_post.json()

response_post.status_code  # requests.codes.ok
response_post.cookies['example_cookie_name']
requests.utils.dict_from_cookiejar(response_post.cookies)  # RequestsCookieJar - > dict
requests.utils.cookiejar_from_dict(dict)  # dict -> RequestsCookieJar`

response_post.request.headers
response_post.headers

# POST一个多部分编码(Multipart-Encoded)的文件
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
r.text
