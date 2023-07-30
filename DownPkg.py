import requests
import sys
import os
header = {'User-Agent' : "Cydia/0.9 CFNetwork/711.5.6 Darwin/14.0.0"}

server = "127.0.0.1"
abc = "LF"
path = "Packages"

try:
    server=sys.argv[1] #服务器地址
    path = sys.argv[2] #目录
    print("服务器:" + server)
    print("目录：" + path)

    
except Exception as q:
    print("遇到错误:" + str(q))


try:
    print("正在下载")
    back = requests.get(server,headers=header)
    print("正在写入")
    with open(path,"wb") as f:
        f.write(back.content)
    print("写入完成")
    
    

except Exception as w:
    print("遇到错误:" , w)