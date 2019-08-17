"""
基本排序算法示例
"""


class Sort:
    def __init__(self, list_):
        self.list_ = list_

    def bubble(self):
        '''
        冒泡排序

        '''
        # 　外层循环表示比较多少轮
        for i in range(len(self.list_) - 1):
            # 　内层循环表示每轮比较的次数
            for j in range(len(self.list_) - i - 1):       #每轮比较确定一个最大值，后面就多一个数不用比较
                # 前一个数比后一个数大则交换位置
                if self.list_[j] > self.list_[j + 1]:
                    self.list_[j], self.list_[j + 1] = \
                        self.list_[j + 1], self.list_[j]

    def select(self):
        '''
        选择排序
        '''
        # 　比较多少轮
        for i in range(len(self.list_) - 1):
            min = i  # 假定i号位置数字最小   通过设定min值可以有效减少序列元素间的交换
            for j in range(i + 1, len(self.list_)):
                if self.list_[min] > self.list_[j]:
                    min = j
            if i != min:
                self.list_[i], self.list_[min] = \
                    self.list_[min], self.list_[i]

    def insert(self):
        '''
        插入排序,就是将一个插入到一个已经排好序的列表中，得到的新列表也是排好序的

        '''
        for i in range(1, len(self.list_)):
            x = self.list_[i]
            j = i
            while j > 0 and self.list_[j - 1] > x:
                self.list_[j] = self.list_[j - 1]#将大于比较的数往后移动一位，copy一份
                j -= 1
            #self.list[j-1]<=x时，说明前面的数都小于x,x正确的位置就是当前j的位置
            self.list_[j] = x #将比较的数放到小于等于这个数的后面一位

    #   my_code
    # def insert_(self):
    #     '''
    #     插入排序,就是将一个插入到一个已经排好序的列表中，得到的新列表也是排好序的
    #     将序列分为2部分，前面为已经排好序的序列，后面为将要插入的数据
    #     '''
    #     for i in range(1, len(self.list_)):       # 这个序列整体无序，所以从第二个开始插入这里
    #         x = self.list_[i]                     # x表示的是需要插入的数据元素
    #         y = i                                 # y 表示的是x实际索引位置，即将被替换的位置，因为i位置的数据已经拿出去比较
    #         for j in range(y - 1, -1, -1):        # x,从i的前一个数开始比较，从后往前。
    #             if self.list_[j] < x:             # 将x与序列元素作比较
    #                 break                         # 如果插入的数据元素比序列倒数第一个元素还大，就直接放到最后面，即原来的位置
    #             self.list_[y] = self.list_[j]     # 如果插入的数没有比较的数大，就和这个数交换位置，直到找到比他小的数，或到头了
    #             y -=1
    #         self.list_[y] = x
    # 一轮交换
    def sub_sort(self, low, high):
        '''
        以序列首个元素为基准，大于的数放后面，小于的数放前面
        low为代表前面（小于key的值），基准前面的位置，high代表后面的位置（大于key的值），当low=high时，为基准的位置
        '''
        key = self.list_[low]  # 基准数字   key
        while low < high:         #实际情况为low  ==  high时跳出循环
            #　后面的数向前甩
            while low < high and self.list_[high] >=key:  #因为key为首位元素，所以先从后面找小于key的元素，
                high -= 1                                  #如果不满足小于（大于等于）key，就往前推移，直到满足条件或者已经
                                                            # 达到low的位置即小于等于key的位置
            self.list_[low] = self.list_[high]              #找到小于key的就将数据元素放到low的位置
            # 　前面的数向后甩
            while low < high and self.list_[low] < key:     #因为high位置的数据元素已经赋值给low位置，这样可以从low位置开始遍历
                                                            #寻找大于key的值赋值给high位置
                low += 1                                    #当不满足大于key的条件时，low向后推移，直到满足条件或者与high相等
            self.list_[high] = self.list_[low]              #将满足大于key的数据元素赋值给high位置，
        self.list_[low] = key                               #依次类推直到low==high 表示当前位置前面的数小于key,后面的数大于等于
        return low                 #返回key的位置                          #key这个位置正好是key现在的位置，

    # 　快速排序函数
    def quick(self, low, high):
        # 　low 列表开头元素索引
        # high 列表结尾元素索引   low，到high之间为需要找key值进行上面操作的区间
        if low < high:          #时间情况为low ==key
            key = self.sub_sort(low, high)     #进行上面操作并key的位置对2两边进行分区
            self.quick(low, key - 1)            #小于key位置值的区间，递归分区，直到low==key-1,
            self.quick(key + 1, high)           #大于key位置值的区间,递归分区，直到key+1==high 即区间只有一个数据元素
                                                #每次quick()方法操作就是确定一个key值的位置，因为都是对列表操作，所以所有操
                                                #作都是在同一个表里进行的

if __name__ == "__main__":
    l = [4, 1, 2, 6, 7, 3, 9, 8,6,2]
    sr = Sort(l)
    # sr.bubble() #　冒泡
    # sr.select() #　选择
   # sr.insert() #　插入
    sr.quick(0, len(l) - 1)
    print(sr.list_)
