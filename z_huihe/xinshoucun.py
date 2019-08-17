from body_1 import *
from yongningcun import yongningcun
from jindutiao import sousuo
def xinshoucun(wuji):
    while True:
        try:
            xuanze=int(input("你是否去郊区打怪练级，1.是的，2.那你继续在新手村转转,3.前往永宁村："))
            if xuanze not in(1,2,3):
                print("你输入的不合规则，默认你选择１")
                xuanze=1
        except:
            print('输入不符合规则，默认为1')
            xuanze=1
        if xuanze==1:
            while True:
                gebulin=Guai("哥布林",100,20,300,80)
                guluguai=Guai("咕噜怪",80,40,400,100)
                bianfu=Guai("嗜血蝙蝠",120,50,300,120)
                bitiguai=Guai("鼻涕怪",70,60,300,80)
                guai_list=[gebulin,guluguai,bianfu,bitiguai]
                suiji_guai=choice(guai_list)
                print('正在搜索....')
                xuanze=int(input("你碰到了一个%s，你是否要消灭它，１．是，２．退出"%suiji_guai.na))
                if xuanze not in(1,2):
                    print("你输入的不合规则，默认你选择１")
                    xuanze=1
                if xuanze==1:
                    dafa=int(input("请选择攻击方式，１．普通攻击，２．释放技能"))
                    if dafa==1:
                        wuji.gongji(suiji_guai)
                        jn=suiji_guai.diao(hbj,hyq)
                        del suiji_guai
                        if jn:
                            print('掉落了一本%s技能书'%jn.na)
                            if jn not in wuji.jn:
                                jn_xz=input('你是否选择：１,是;2,否：')
                                if jn_xz=="1":
                                    wuji.get_skill(jn)
                                else:
                                    pass
                            else:
                                print("但是你已经掌握了该技能")
                    else:
                        if wuji.jn:
                            wuji.re_skill(wuji.jn[0],suiji_guai)
                            del suiji_guai
                        else:
                            print("你没有技能，你只能普通攻击")
                            wuji.gongji(suiji_guai)
                            del suiji_guai
                else:
                    print("你退出了郊区,前往新手村")
                    break

        elif xuanze==2:
            print('你在新手村浪费了一天时间')
        else:
            if wuji.dengji>=10:
                yongningcun(wuji)
                return
            else:
                print("等级不够，请继续在新手村练级吧")
                xinshoucun(wuji)