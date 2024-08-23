import re
import requests

# 从文本文件中读取IP地址
def read_targets_from_file(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

# 用于批量提交flag的API地址和API密钥
flag_submit_url = "" #flag提交平台网址
api_key = "" #队伍ID，如果没用则留空

# payload
rce_payload = ""

# 获取并提交flag的函数
def exploit_and_submit(target):
    try:
        # 执行RCE攻击，设置超时时间（例如5秒）
        r = requests.get(target + rce_payload, timeout=10)
        
        # 根据具体情况提取flag
        flag = extract_flag(r.content)

        # 提交flag
        if flag:
            submit_flag(flag)
        else:
            print(f"无法从此IP获取flag: {target}")
    except requests.exceptions.RequestException as e:
        print(f"执行错误: {target}: {e}")


# 从RCE攻击响应中提取flag的函数
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
            print(f"提交成功: {flag}")
        else:
            print(f"提交失败: {r.content}")
    except Exception as e:
        print(f"提交错误: {e}")

# 将目标列表从文本文件中读取
targets_file = "ips.txt"
targets = read_targets_from_file(targets_file)

# 遍历目标列表并执行RCE攻击
for target in targets:
    exploit_and_submit(target)
