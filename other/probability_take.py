'''
    利用random模块随机取数，按照要求有概率，比如2个数之间取数，两个数的概率不相等
'''
from random import randint
from random import choice


def get_2_4():
    '''
    随机产生数字2个数
    取2的概率为90%
    取4的概率为10%
    :return:
    '''
    return 4 if randint(1,9) ==1 else 2  #randint(1,9)

def get_number(number1,number2,fun):
    '''
    泛化 根据条件取2个数
    :param number1:
    :param number2:
    :param fun: 条件函数
    :return:
    '''
    return number1 if fun() else number2


# for i in range(10):
#    print(get_number(1,2,lambda :randint(1,9)>5))

def get_number2(list01):
    '''
    这个就是看看，可以活用random模块中的choice 方法，
    从列表中随机取数，根据自己的要求传入相应的；列表元素
    :param list01:
    :return:
    '''
    return choice(list01)
