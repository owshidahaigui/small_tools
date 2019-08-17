"""
    ui
"""

from bll import GameCoreController
from model import Direction
import os

class GameConsoleView:
    """
        控制台视图
    """

    def __init__(self):
        # 　创建核心类对象
        self.__controller = GameCoreController()

    def start(self):
        """
            游戏开始
        """
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__print_map()

    def __print_map(self):
        # 清空控制台
        os.system("clear")
        for r in range(len(self.__controller.map)):
            for c in range(len(self.__controller.map[r])):
                print(self.__controller.map[r][c], end="\t")
            print()

    def update(self):
        """
            更新(游戏逻辑)
        :return:
        """
        while True:
            self.__move_map()
            # if 界面发生变化
            #这个判断用于避免玩家在一个方向已经不能合成，
            #通过不断使用那个方向键来生成新的随机数，
            # 避免出现，比如一直按‘上’明明已经没法合成了，却能产生随机数
            if self.__controller.is_change:
                self.__controller.generate_new_number()
                self.__print_map()
                #下边步鄹用于正确操作后，系统直接判断是否存在再次合成的可能
                #如果没有相邻合成的可能确没有
                if self.__controller.is_game_over():
                    print("游戏结束")
                    break

    def __move_map(self):
        dir = input("请输入移动方向(wsad)")
        if dir == "w":
            self.__controller.move(Direction.up)
        elif dir == "s":
            self.__controller.move(Direction.down)
        elif dir == "a":
            self.__controller.move(Direction.left)
        elif dir == "d":
            self.__controller.move(Direction.right)
