
#celery_app 异步队列使用
#启动work  'celery worker -A celery_app -l INFO'

import time

from celery_app  import task1,task2


task1.add.delay(2,4)

task2.multiply.delay(4,5)

print('end....')
# if __name__=='__main__':
# 	print('start task....')
# 	result = add.delay(3,8)
# 	print('end task')
# 	print(result)