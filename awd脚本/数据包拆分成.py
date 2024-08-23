header = {}
url = "http://127.0.0.1/upload-labs/Pass-01/index.php"
with open('header.txt','r') as file:
    header_raw = file.read()
with open('pakge.txt', 'r') as file:
    data = file.read()
# print(header_raw.find('\n'))
# print(header_raw.find(':'))
# header_value = header_raw[12:header_raw.find('\n')]
# print(header_value)
# print(header_raw[header_raw.find('\n')+1:])
while True:
    header_title = header_raw[:header_raw.find(':')]
    header_value = header_raw[header_raw.find(':') + 2:header_raw.find('\n')]
        # print(header_title)
        # print(header_value)
    if(header_raw.find(':') + 1 == 0):
        print('header is end')
        break
    header[header_title] = header_value
    header_raw = header_raw[header_raw.find('\n') + 1:]
    # print(header)
# header['data'] = data
print(header)
# print(type(data))
# data = {'key1': 'value1', 'key2': 'value2'}