# requests POST请求

import requests
import json

# POST请求的url同get请求，参数有一下几种
# 1、字典类型
data0 = {"k1": "v1", 'k2': 'v2', 'k3': 'v3'}

# 2、元组或者列表
data1 = (('k1', 'v1'), ('k2', 'v2'))

# 3、Json类型
data2 = {"k1": "v1", 'k2': 'v2', 'k3': 'v3'}
data3 = json.dumps(data2)

response0 = requests.post("https://www.baidu.com/", data=data3)
# print(response0.text)  # 返回HTML源码  str类型
# print(type(response0.text))

#  requests的POST还有其他参数可以输入
#  requests的POST还有其他参数可以输入
#  requests的POST还有其他参数可以输入

#  1、增加头部 headers、 使用代理IP、证书验证、超时设置、cookie

# 增加头部
headers = {
    'Content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;'
                  ' x64) AppleWebKit/537.36 (KHTML, like'
                  ' Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Cookie': 'BDUSS=pIeTNWNWlLczRUMy03eFVWWXVtUWcyTkY3Q3VxUnNsVWJIT3lueW5HRDJzQkpsRVFBQUFBJCQAAAAAAAAAAAEAAADT5z6EdXR0Zmh1ZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPYj62T2I-tkTm; BDUSS_BFESS=pIeTNWNWlLczRUMy03eFVWWXVtUWcyTkY3Q3VxUnNsVWJIT3lueW5HRDJzQkpsRVFBQUFBJCQAAAAAAAAAAAEAAADT5z6EdXR0Zmh1ZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPYj62T2I-tkTm; BAIDUID=5778C7EC5E2BF528E41894641161CFA7:SL=0:NR=10:NW=Y:NEWS=Y:SU=3:FG=1; sug=3; sugstore=1; ORIGIN=0; bdime=0; MCITY=-218%3A; channel=bing; baikeVisitId=d299e5e9-5a1d-46eb-bec5-549ed0ead1bf; COOKIE_SESSION=32_0_8_8_7_28_0_0_8_8_3_7_3959557_0_0_0_1696391023_0_1702555750%7C9%230_0_1702555750%7C1; __bid_n=1864e04bd42e3401ce4207; BAIDUID_BFESS=5778C7EC5E2BF528E41894641161CFA7:SL=0:NR=10:NW=Y:NEWS=Y:SU=3:FG=1; BAIDU_WISE_UID=wapp_1703857399182_718; ZFY=agOGoo2t7KDraFRuuytVXYCKx1T4PAFJu19:B06SvYKI:C; RT="z=1&dm=baidu.com&si=7bb42ce6-bc21-4730-bd32-3d2c71fe5602&ss=lwbxjz2u&sl=d&tt=399&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1vvh&ul=6zgs&hd=70vv"; PSTM=1716184957; H_PS_PSSID=40463_60270_60289; BD_UPN=12314753; BIDUPSID=B03633E383B2373E585F3C38221E0482; BA_HECTOR=8l8g24258lah812l04048h84f14atk1j4ogf31v; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'  ## 这里也可以设置cookie
}
response1 = requests.post("https://www.baidu.com/", data=data3, headers=headers)

# 使用代理

proxies = {
    'http': 'http://10.10.11.1:2342',
    'https': 'https://10.12.11.2:2345'
}
response2 = requests.post("https://www.baidu.com/", data=data3, headers=headers, proxies=proxies)
print(response2.text)

# 证书验证
# 1、不验证：verify=False   2、验证 verify=True   3、设置证书路径 verify='/path/certfile'
response3 = requests.post("https://www.baidu.com/", verify=False)

# 超时设置 timeout=0.01  单位 s
response4 = requests.post("https://www.baidu.com/", timeout=0.01)


