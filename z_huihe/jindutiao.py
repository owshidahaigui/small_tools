from time import sleep
from random import randint
def sousuo():
    i=randint(1,30)
    print(i)
    for x in range(1,i):
        print(x*' '+'正在搜索', end='\r')
        sleep(1)
if __name__ == '__main__':
    sousuo()
    # print(1 * '    ' + '正在搜索', end='\r')
    # sleep(2)
    # print(2 * '     ' + '正在搜索', end='\r')