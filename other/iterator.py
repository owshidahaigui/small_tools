class Iteration:
    '''
    迭代器类
    '''
    def __init__(self, it_list):
        self.__it_list = it_list
        self.index = 0

    def __next__(self):
        if self.index > len(self.__it_list) - 1:
            raise StopIteration
        i = self.__it_list[self.index]
        self.index += 1
        return i
