import requests


url = ''

data = {
    "data":[
        {
            "xxx":"xxx",
            "xxx":"xxx",
        }
    ]
}
res = requests.post(url,json=data)
print(res.text)