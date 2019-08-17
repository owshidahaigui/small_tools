from random import choice
from random import randint

class GameCore:
    '''
    游戏核心控制器
    '''

    def __init__(self, length=4):
        self.length = length
        self.list_2048 = [[0] * self.length for i in range(length)]
        self.update_number()
        self.update_number()

    def update_number(self):
        '''
        随机选择某个零位置，将其随机赋值（2,4）
        :param new_list:
        :return:
        '''
        list_zero = []
        for i in range(self.length):
            for x in range(self.length):
                if self.list_2048[i][x] == 0:
                    list_zero.append((i, x))
        random_tuple = choice(list_zero)
        self.list_2048[random_tuple[0]][random_tuple[1]] = GameCore.new_number()

    @staticmethod
    def new_number():
        '''
        从列表中随机选取一个数返回
        :return:
        '''
        return choice([4, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        #return choice 4 if random.randint(1,10)==1  else 2)

    @staticmethod
    def zero_to_end(list_2048):
        '''
        列表中的所有非零数都往左靠，零往右靠，列表长度不变
        :param self:
        :return:
        '''
        zero_count = list_2048.count(0)
        for i in range(zero_count):
            list_2048.remove(0)
        list_2048 += ([0] * zero_count)

    @staticmethod
    def merge(list_2048):
        '''
        列表中的相邻的相同数字相加，非零数都在左边，列表长度不变
        :param self:
        :return:
        '''
        GameCore.zero_to_end(list_2048)
        for i in range(len(list_2048) - 1):
            if list_2048[i] == list_2048[i + 1]:
                list_2048[i] += list_2048[i + 1]
                list_2048[i + 1] = 0
        GameCore.zero_to_end(list_2048)

    def move_right(self):
        '''
        将2维列表中的每个一维列表都
        :param self:
        :return:
        '''
        for j in range(self.length):  # 按行进行
            list02 = self.list_2048[j][::-1]
            GameCore.merge(list02)
            self.list_2048[j][::-1] = list02

    def move_left(self):
        for j in self.list_2048:  # 按行进行
            GameCore.merge(j)

    # i 为列  x 为行
    def move_up(self):
        for i in range(self.length):
            list02 = []
            for x in range(self.length):
                list02.append(self.list_2048[x][i])
            GameCore.merge(list02)
            for x in range(self.length):
                self.list_2048[x][i] = list02[x]

    # i 为列  x为行
    def move_down(self):
        for i in range(self.length):
            list02 = []
            for x in range(self.length - 1, -1, -1):
                list02.append(self.list_2048[x][i])
            GameCore.merge(list02)
            for x in range(self.length - 1, -1, -1):
                self.list_2048[x][i] = list02[self.length - 1 - x]

    # def count_score(self):
    #     sum =0
    #     for i in range(self.length):
    #         for r in range(self.length):
    #             sum+= self.list_2048[i][r]
    #     return sum
