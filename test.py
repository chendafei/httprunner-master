# coding=utf-8
import requests
import json
from time import time
import threading
import csv

data = {
            "coin_type": "BSV",
            "flat_amount": "99900",
            "totp_captcha": {"validate_code": "111111", "sequence": ""}
            }

# 定义需要进行发送的数据

# 定义一些文件头
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': '53383C06B6E449FFB5444432B456F72E'
           }

# 创建请求函数
def Clean():
    # 接口的url
    requrl = "http://test2.coinex.com/res/credit/to/flat?X-CSRF-TOKEN=DI12i7hp"
    # 连接服务器
    # 发送请求
    response = requests.post(requrl, headers=headers, data=json.dumps(data))
    # 打印请求状态
    print(response.json())


# 创建数组存放线程
threads = []
# 创建100个线程
for i in range(50):
    # 针对函数创建线程
    t = threading.Thread(target=Clean, args=())
    # 把创建的线程加入线程组
    threads.append(t)

# print（'start:'）
if __name__ == '__main__':
    # 启动线程
    for i in threads:
        i.start()
        # keep thread
    for i in threads:
        i.join()

#print('end:', ctime())