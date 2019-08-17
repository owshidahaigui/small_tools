import time 

#导入app文件
from celery_app import app

@app.task
def add(x,y):
	print('start')
	time.sleep(3)
	print('end')
	return x+y