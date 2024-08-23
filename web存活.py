import requests
import ipaddress

ip_net = input('please enter ip:(example:172.18.140.201/24)\n')
net = ipaddress.ip_network(ip_net, strict=False)
ip = [x for x in net.hosts()]
url_header = "http://"

# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
length = len(ip)
for i in range(length):
    #print(ip[i])
    url = url_header + str(ip[i])
    #print(url)
    try:
        r = requests.get(url, headers=headers)
        if r != '':
            print(url)
    except:
        print(end='')