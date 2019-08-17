class StudentModel:
    '''
    学生数据模型类
    '''

    def __init__(self, name='', age=0, score=0, id=0):
        '''
        创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        '''
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


class StudentManagerController:
    '''
    学生逻辑控制类
    '''

    def __init__(self):
        '''
        创建学生列表
        '''
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list[:]

    def add_student(self, student):
        '''
        增加学生
        :param student:
        :return:
        '''
        student.id = self.__greate_student_id()
        self.__stu_list.append(student)

    def __greate_student_id(self):
        '''
        获取学生编号
        :return:
        '''
        return self.__stu_list[-1].id + 1 if len(self.__stu_list) > 0 else 1

    def search_student(self, id):
        for x in self.__stu_list:
            if id == x.id:
                return x

    def remove_student(self, id):
        '''
        删除学生对象
        :param student:
        :return:
        '''
        if self.search_student(id):
            self.__stu_list.remove(self.search_student(id))
            return True

    def update_student(self,id,proper,value):
        '''
        修改学生
        :return:
        '''
        for item in self.__stu_list:
            if item.id == id :
                if proper=='name':
                    item.name=value
                elif proper =='age':
                    item.age=value
                elif proper =='score':
                    item.score=value
                return True


    def order_by_score(self):
        stu_list_copy = self.__stu_list.copy()
        for x in range(len(stu_list_copy) - 1):
            for i in range(x + 1, len(stu_list_copy)):
                if stu_list_copy[x].score < stu_list_copy[i].score:
                    stu_list_copy[x], stu_list_copy[i] = stu_list_copy[i], stu_list_copy[x]
        return stu_list_copy


class StudentManagerView:
    """
        界面视图类
    """

    def __init__(self):
        # 创建逻辑控制器对象
        self.__manager = StudentManagerController()

    def __input_students(self):
        # 1. 在控制台中录入学生信息,存成学生对象StudentModel.
        # 2. 调用逻辑控制器的add_student方法
        # self.__manager.add_student(学生对象)
        name = input('请输入学生姓名')
        age = int(input('请输入学生年龄'))
        score = int(input('请输入学生成绩'))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __delete_student(self):
        id = int(input('请输入需要删除的学生编号'))
        self.__manager.remove_student(id)
        if self.__manager.remove_student(id):
            print('删除成功')
        else:
            print('删除失败')

    def __modify_student(self):
        id = int(input('请输入需要修改学生的编号'))
        proper=input(r'请输入需要修改的属性name\age\score')
        if proper=='name':
            value=input('请输入修改的结果')
        else:
            value=int(input('请输入修改的结果'))
        a=self.__manager.update_student(id,proper,value)
        if a :
            print('修改成功')
        else:
            print('修改失败')


    def __output_student_by_score(self):
        manger_copy = self.__manager.order_by_score()
        self.__print_manager(manger_copy)

    def __display_menu(self):
        """
            显示菜单
        :return:
        """
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩降序排列")

    def __select_menu(self):
        """
        选择菜单
        :return:
        """
        number = input("请输入选项:")
        if number == "1":
            self.__input_students()
        elif number == "2":
            self.__print_manager(self.__manager.stu_list)
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__modify_student()
        elif number == "5":
            self.__output_student_by_score()

    def __print_manager(self, list_targer):
        print()
        for x in list_targer:
            print('学生编号', x.id, '学生姓名', x.name, '学生年龄', x.age, '学生成绩', x.score)
        print()

    def main(self):
        """
            界面入口方法
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()


view = StudentManagerView()
view.main()
