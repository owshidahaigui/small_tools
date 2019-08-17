"""
ftp　文件服务器
并发网络功能训练
"""

from socket import *
from threading import Thread
import os
from time import sleep

# 　全局变量
HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST, PORT)
FTP = "/home/tarena/桌面/test/z_ftp/"  # 文件库路径


# 将客户端请求功能封装为类
class FtpServer:
    def __init__(self, connfd, FTP_PATH):
        #传入对应套接字
        self.connfd = connfd
        #传入文件夹路径   对应库的路径
        self.path = FTP_PATH

    def do_list(self):
        #　获取文件列表
        files = os.listdir(self.path)
        if not files:
            self.connfd.send("该文件类别为空".encode())
            return

        self.connfd.send(b'OK')
        sleep(0.1)
        fs = ''
        #将文件列表转换为一个字符串发送
        for file in files:
            #要求是普通文件且不是隐藏文件   要求绝对路径
            if file[0] != '.' and os.path.isfile(self.path+file):
                #用转义换行符将文件名隔开
                fs += file + '\n'
        self.connfd.send(fs.encode())

    def do_get(self,filename):
        try:
            fd = open(self.path+filename,'rb')
        except Exception:
            self.connfd.send('文件不存在'.encode())
            return

        self.connfd.send(b'OK')
        #延迟一秒防止粘包
        sleep(0.1)
        #　发送文件内容
        while True:
            data = fd.read(1024)
            if not data:  #　文件结束
                sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    def do_put(self,filename):
        if os.path.exists(self.path + filename):
            self.connfd.send("该文件已存在".encode())
            return
        self.connfd.send(b'OK')
        fd = open(self.path + filename,'wb')
        # 接收文件
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            print(data)
            fd.write(data)
        print('上传成功')
        fd.close()

# 客户端请求处理函数
def handle(connfd):
    # 　选择文件夹
    cls = connfd.recv(1024).decode()
    #获取路径,进入指定库
    FTP_PATH = FTP + cls + '/'
    #创造功能类对象
    ftp = FtpServer(connfd, FTP_PATH)
    while True:
        # 接受客户端命令请求
        data = connfd.recv(1024).decode()
        #　如果客户端断开返回ｄａｔａ为空，空的话无法用索引
        if not data or data[0] == 'Q':
            return
        elif data[0] == 'L':
            ftp.do_list()
        elif data[0] == 'G':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[0] == 'P':
            filename = data.split(' ')[-1]
            ftp.do_put(filename)


# 网络搭建
def main():
    # 　创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("Listen the port 8080...")
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            print("退出服务程序")
            return
        except Exception as e:
            print(e)
            continue
        print("链接的客户端：", addr)
        # 　创建线程处理请求
        client = Thread(target=handle, args=(connfd,))
        client.setDaemon(True)
        client.start()


if __name__ == "__main__":
    main()
