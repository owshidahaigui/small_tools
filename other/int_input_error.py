
def get_score(self):
    '''
    对所有数字输入进行排除数字输入时的错误输入造成的程序中断
    :param self:
    :return:
    '''
    while True:
        try:
            number = int(input("请输入成绩:%s"%self))
        except:
            # print("输入有误")
            continue # 跳过本次循环
        # if 1<= number <= 100:
            return number
        # print("成绩不在范围内")

