import hashlib
# md5 = hashlib.md5()     # 应用MD5算法（sha1,sha256,sha384,sha512等）
# data_1 = "hello world"
# md5.update(data_1.encode('utf-8'))
# data_2=md5.hexdigest()
# print(data_2)
# print(type(data_2))

# md5.update(data_1.encode('utf-8'))
# data_3=md5.hexdigest()
# print(data_3)
# print(type(data_3))

# # 加盐加密：
# hash = hashlib.md5('abc'.encode('utf-8'))
# hash.update("hello world".encode('utf-8'))
# print(hash.hexdigest())


def md5(arg):#这是加密函数，将传进来的函数加密
    md5_pwd = hashlib.md5('abd'.encode('utf-8'))
    md5_pwd.update(arg.encode('utf-8'))
    return md5_pwd.hexdigest()#返回加密的数据
def log(user,pwd):#登陆时候时候的函数，由于md5不能反解，因此登陆的时候用正解
    with open('db','r',encoding='utf-8') as f:
        for line in f:
            u,p=line.strip().split('|')
            if u ==user and p == md5(pwd):#登陆的时候验证用户名以及加密的密码跟之前保存的是否一样
                return True
        return False

def register(user,pwd):#注册的时候把用户名和加密的密码写进文件，保存起来
    with open('db','a',encoding='utf-8') as f:
        temp = user+'|'+md5(pwd)
        f.write(temp)
        f.write('\n')
def main():
    while True:
        print('''1登陆
2注册
3退出
        ''')
        i=input('请选择')
        if i=='2':
            user = input('用户名：')
            pwd =input('密码：')
            register(user,pwd)
        elif i=='1':
            user = input('用户名：')
            pwd =input('密码：')
            r=log(user,pwd)#验证用户名和密码
            if r ==True:
                print('登陆成功')
            else:
                print('登录失败')
        elif i=='3':
            print('选择退出')
            break
        else:
            print('账号不存在')

if __name__=='__main__':
    main()
