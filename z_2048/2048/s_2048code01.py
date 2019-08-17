from gane_contrill import *
from copy import deepcopy


class GameView:

    def __init__(self, length=4):
        self.__game_list_c = GameCore(length)
        self.__length = length

    def __game_choice(self):
        cmds = {'w': self.__game_list_c.move_up,
                's': self.__game_list_c.move_down,
                'a': self.__game_list_c.move_left,
                'd': self.__game_list_c.move_right
                }
        chioce = input('请输入你的选择w,a,s,d')
        if chioce in cmds:
            cmds[chioce]()

    def __print_map(self):
        '''
        将2维列表以表格形式打印列表
        :param self:
        :return:
        '''
        for i in range(self.__length):
            for r in range(self.__length):
                print(self.__game_list_c.list_2048[i][r], end=' ')
            print()

    def main(self):
        while True:
            self.__print_map()
            list_copy = deepcopy(self.__game_list_c.list_2048)
            self.__game_choice()
            if list_copy == self.__game_list_c.list_2048:
                print('游戏结束')
                break
            self.__game_list_c.update_number()

if __name__ == '__main__':
    GameView().main()
