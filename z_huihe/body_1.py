from random import choice
from time import sleep
class Human():
    '''这是人物类'''
    def __init__(self,name,gj,fy,xl,lan,score=0,dengji=1):
        self.na=name
        self.gj=gj
        self.fy=fy
        self.xl=xl
        self.lan=lan
        self.score=score
        self.dengji=dengji
        self.n=100
        self.al="y"
        self.jn=[]
        self.xianshi()

    def xianshi(self):
        print('      $     名字是：', self.na)
        print('      $     攻击力：',self.gj)
        print('      $     防御力：', self.fy)
        print('      $     血量：', self.xl)

    def jingyan(self,n):
        self.score+=n
        if self.score>=self.n:
            self.dengji+=1
            self.n+=50
            self.gj+=10
            self.fy+=10
            self.xl+=100
            self.lan+=70
            self.score=self.score%self.n
            print("☯　☯　☯　☯　恭喜%s升到%s级☯　☯　☯　☯"%(self.na,self.dengji))
            self.xianshi()
        else:
            print("%s获取了%s经验"%(self.na,n))
            print("经验条"+"▓▓▓▓"*int(10*self.score/self.n))

    def get_skill(self,jn):
        print('88888888')
        self.jn.append(jn)
        print("装备技能成功")

    def gongji(self,name):
        if self.al=="n":
            print("%s已经死亡,无法攻击"%self.na)
        elif name.al=="n":
            print("%s已经死亡"%name.na)
        else:
            print("***********%s成功攻击%s***********"%(self.na,name.na))
            while name.xl>0:
                n=self.gj-name.fy
                if n<0:
                    n=0
                name.xl=name.xl-n
                if name.xl<=0:
                    name.xl=0
                    name.al='n'
                    print("%s已被杀死"%name.na)
                    self.jingyan(name.score)
                else:
                    print("%s血量剩余%s"%(name.na,name.xl))
                    sleep(0.5)
                    print("轮到%s攻击%s"%(name.na,self.na))
                    n1=name.gj-self.fy
                    print('怪物的攻击与任务防御差值%s'%(n1))
                    if n1<0:
                        n1=0
                    self.xl-=n1
                    if self.xl<=0:
                        self.xl=0
                        self.al='n'
                        print("%s已被杀死,游戏结束"%self.na)
                    else:
                        print("%s血量剩余%s"%(self.na,self.xl))
                        print("轮到%s攻击%s"%(self.na,name.na))
                        sleep(0.5)

    def re_skill(self,jn,name):
        while name.xl>0:
            if jn in self.jn:
                if self.al=="n":
                    print("%s已经死亡"%self.na)
                    break
                elif name.al=="n":
                    print("%s已经死亡"%name.na)
                    break
                else:
                    if self.lan>=jn.lan:
                        self.lan-=jn.lan
                        n=self.gj*jn.gj-name.fy
                        if n<0:
                            n=0
                        print('释放%s技能'%(jn.na))
                        name.xl=name.xl-n
                        if name.xl<=0:
                            name.xl=0
                            name.al='n'
                            print("%s已被杀死"%name.na)
                            self.jingyan(name.score)
                        else:
                            print("%s血量剩余%s"%(name.na,name.xl))
                            sleep(0.5)
                            print("轮到%s攻击%s"%(name.na,self.na))
                            n1=name.gj-self.fy
                            if n1<0:
                                n1=0
                            self.xl-=n1
                            if self.xl<=0:
                                self.xl=0
                                self.al='n'
                                print("%s已被杀死,游戏结束"%self.na)
                            else:
                                print("%s血量剩余%s"%(self.na,self.xl))
                                print("轮到%s攻击%s"%(self.na,name.na))
                                sleep(0.5)
     #===================================================
                    else:
                        print("%s没蓝了,释放技能失败,继续普通攻击"%self.na)
                        self.gongji(name)
                        break
            else:
                print("你还没有学习%s技能,只能普通攻击"%jn.na)
                self.gongji(name)

    def wq(self,wuqi):
        print("%s装备了%s"%(self.na,wuqi.na))
        self.gj+=wuqi.gj
        self.fy+=wuqi.fy
        self.xl+=wuqi.xl

    def del_wq(self,wuqi):
        print("%s脱下了%s"%(self.na,wuqi.na))
        self.gj-=wuqi.gj
        self.fy-=wuqi.fy
        self.xl-=wuqi.xl



class Wuqi():
    '''这是武器类'''
    def __init__(self,name,gj,fy,xl):
        self.na=name
        self.gj=gj
        self.fy=fy
        self.xl=xl

class Jn():
    '''这是技能类'''
    def __init__(self,name,n,lan):
        self.na=name
        self.gj=n
        self.lan=lan

class Guai():
    def __init__(self,name,gj,fy,xl,score):
        self.na=name
        self.gj=gj
        self.fy=fy
        self.xl=xl
        self.score=score
        self.al="y"

    def diao(self,jn1,jn2):
        print('执行装备掉落程序')
        n=choice(list(range(1,11)))
        b=choice([jn1,jn2])
        print(n)
        if n>=6:
            return b
        else:
            return

tl=Wuqi("屠龙宝刀",40,40,600)
hb=Wuqi("寒冰护甲",10,70,600)
sq=Wuqi("神器",300,300,1000)
sq.asdasd='adasd'

hbj=Jn("寒冰箭",1.3,150)
hyq=Jn("火焰枪",1.5,200)