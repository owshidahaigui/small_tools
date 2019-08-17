from celery import Celery

broker='redis://localhost:6379/1'
backend='redis://localhost:6379/2'

#jiangAPP
app=Celery('demo')
#通过Celery 实例加载配置模块
app.config_from_object('celery_app.celery_config')
