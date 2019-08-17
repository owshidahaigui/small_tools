cmds = {
    '摩柯无量': ['Damage(80)', 'Sarcasm(50)'],
    '小无相功': ['Damage(120)', 'Sarcasm(60)']
}


class SkillCreate:


    def __init__(self, name):
        self.name = name
        self.__list_skill=self.__create_skill()

    def __create_skill(self):
        return [eval(item) for item in  cmds[self.name]]


    def release_skill(self):
        for i in self.__list_skill:
            print('使用%s'%(self.name),end='')
            i.result()


class SkillResult:
    def __init__(self, value):
        self.value = value

    def result(self):
        pass


class Sarcasm(SkillResult):
    '''
    嘲讽效果
    '''

    def result(self):
        print('对敌人造成%s范围的嘲讽效果' % self.value)


class Damage(SkillResult):
    def result(self):
        print('对敌人造成%s点伤害' % (self.value))


s1=SkillCreate('摩柯无量')
s1.release_skill()