

#导入定时器
from datetime import timedelta
from celery.schedules import crontab
#设置,队列存储

BROKER_BACKEND='redis'
#
BROKER_URL='redis://localhost:6379/1'

CELERY_RESULT_BACKEND='redis://localhost:6379/2'

CELERY_TIMEZONE='Asia/Shanghai'

#增加要使用的方法
CELERY_IMPORTS=(
	'celery_app.task1',
	'celery_app.task2'
	)

#定时任务添加
CELERYBEAT_SCHEDULE={
	#设置第一个任务
	'task1':{
		#任务函数地址
		'task':'celery_app.task1.add',
		#设置时间
		'schedule':timedelta(seconds=5),
		#导入函数参数
		'args':(2,8)
	},
	'task2':{
	'task':'celery_app.task2.multiply',
	#设置到每天的19时,28分
	'schedule':crontab(hour=18,minute=12),
	'args':(4,5)
	}
}