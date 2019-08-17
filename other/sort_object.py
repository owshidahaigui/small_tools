def sort_object():
    '''
    根据对象的某个属性对对象列表进行选择排序
    :return:
    '''
    for r in range(len(list_skills) - 1):  #遍历第一个到倒数第二个对象
        for c in range(r + 1, len(list_skills)):  #每个遍历出来的对象要求与他后面的进行排序
            if list_skills[r].time  >  list_skills[c].time:  #属性比较
                list_skills[r],list_skills[c] =  list_skills[c],list_skills[r]
                #对象交换