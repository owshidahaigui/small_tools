import time 

#导入app文件
from celery_app import app

@app.task
def multiply(x,y):
	print('start')
	time.sleep(4)
	print('end')
	return x*y