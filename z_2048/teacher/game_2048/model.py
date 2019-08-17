"""
    数据模型模块
"""


class Location:
    """
        位置类   位置封装
    """

    def __init__(self, r, c):
        self.r_index = r
        self.c_index = c

    @property
    def r_index(self):
        return self.__r_index

    @r_index.setter
    def r_index(self, value):
        self.__r_index = value

    @property
    def c_index(self):
        return self.__c_index

    @c_index.setter
    def c_index(self, value):
        self.__c_index = value

# 扩展：枚举   还能用枚举优化
class Direction:
    """
        方向  通过创造类和成员，方便调用人员使用
    """
    up = 0
    down = 1
    left = 2
    right = 3
