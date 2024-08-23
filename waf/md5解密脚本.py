import hashlib
import sys

if len(sys.argv) < 2:
    print("请输入要计算MD5哈希值的字符串。")
else:
    input_str = sys.argv[1]
    md5_hash = hashlib.md5(input_str.encode()).hexdigest()
    print(f"Input string: {input_str}")
    print(f"MD5 hash: {md5_hash}")