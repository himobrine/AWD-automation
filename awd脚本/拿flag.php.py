import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}


for i in range(254,255):
    url = 'http://3.1'
    url = url + '.' +str(i) + '.' + str(16) +
    print(url)
    try:
        r = requests.get(url, headers=headers)
        print(url)
        #print(r.text)
    except:
        print(end='')