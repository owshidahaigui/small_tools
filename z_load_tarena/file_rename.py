
'''
给文件递归改名
'''

import os
from urllib import parse

# style_list = ['pdf', 'md', 'txt']


def file_rename(file_path):
    try:
        file_name_list = os.listdir(file_path)
    except Exception as e:
        return
    for file_name in file_name_list:
        # print(file_name)
        # 判断改名条件
        if '%' in file_name:
            # for style in style_list:
            #     if file_name.endswith(style):
            #         new = parse.unquote(file_name) + '.' + style
            #         new = os.path.join(file_path, new)
            #         old = os.path.join(file_path, file_name)
            #         os.rename(old, new)
            # else:
            new = parse.unquote(file_name)
            new = os.path.join(file_path, new)
            old = os.path.join(file_path, file_name)
            try:
                os.rename(old, new)
            except Exception as e:
                print(e)
                continue
            # print(new)
            file_name = new
        else:
            file_name = os.path.join(file_path, file_name)
        file_rename(file_name)


if __name__ == '__main__':
    file_rename('/home/tarena/桌面/AIDCode/aid1902')
