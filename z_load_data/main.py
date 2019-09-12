'''
类达内笔记下载器
'''

import pymysql
import requests
import random
import time
from lxml import etree
import os
from urllib import parse


class Tarena_code:

    def __init__(self):
        self.url = 'http://code.tarena.com.cn/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        self.auth = ('tarenacode', 'code_2019')
        # self.db = pymysql.connect(
        #     'localhost', 'root', '123456', 'biji', charset='utf8'
        # )
        # self.cursor = self.db.cursor()

    # 得到网页数据或者下载的内容
    def get_code(self, url):
        res = requests.get(url, headers=self.headers, auth=self.auth)
        data = res.content
        return data
        # for parse_link in parse_list:
        #   url=self.url+parse_link

    # 如果是网页就进行分析，
    def parse_data(self, html):
        parse_html = etree.HTML(html)
        parse_list = parse_html.xpath('//a[@href!="../"]/@href')
        print(parse_list)
        return parse_list

    # 下载内容，保存到本地
    def write_data(self, data, url):
        print('开始下载', url)
        filename = url.split('/')[-1]
        # 中文字符转码
        if '%' in filename:
            filename = parse.unquote(filename)
        directory = '/home/tarena/桌面/' + \
            '/'.join(url.split('/')[3:-1]) + '/'
        # 判断路径是否存在
        if not os.path.exists(directory):
            # 递归创建文件夹
            os.makedirs(directory)
        filename = directory + filename
        with open(filename, 'wb') as fd:
            fd.write(data)
            print(url, '下载完成')
        # 下载完成文件路径存入数据库
        # ins = 'insert into urls values(%s)'
        # self.cursor.execute(ins,[url])
        # self.db.commit()

    def main(self, url):
        # 根据路由判断是否为文件夹还是文件
        if url[-1] == '/':
            data = self.get_code(url).decode('utf-8', 'ignore')
            parse_list = self.parse_data(data)
            # 遍历得到的超链接进行爬取
            for x in parse_list:
                url1 = url + x
                print('进入', url1)
                self.main(url1)
        else:
            # 判断文件路径是否存在数据库
            # sel = 'select * from urls where address="{}"'.format(url)
            # self.cursor.execute(sel)
            # if self.cursor.fetchall():
            #     return
            data = self.get_code(url)
            self.write_data(data, url)


if __name__ == '__main__':
    url = 'http://code.tarena.com.cn/AIDCode/aid1903/15_pandas/'
    start = time.time()
    t = Tarena_code()
    t.main(url)
    # data = t.get_code(url)
    # print(t.parse_data(data))
    end = time.time()
    print(end - start)
