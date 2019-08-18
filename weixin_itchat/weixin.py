import itchat
import time
#登陆微信，采用热加载的方式登陆微信，会生成一个itchat.pkl文件，用于保存登陆状态。
itchat.auto_login(hotReload=True)
boom_name = input('输入你想轰炸的基友：')
boom_message = input('输入你想轰炸的消息：')
boom_obj = itchat.search_friends(remarkName=boom_name)[0]['UserName']
while True:
	time.sleep(0.5)
	print('正在轰炸。。。。')
	itchat.send_msg(msg=boom_message,toUserName=boom_obj)
	itchat.revoke
