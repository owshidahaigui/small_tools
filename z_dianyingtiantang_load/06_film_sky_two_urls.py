from urllib import request
import re
import time
import random
from fake_useragent import UserAgent
import pymysql
import redis

import execjs
# 电影天堂电影数据爬取


class FilmSky(object):
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        # 定义两个对象
        # self.db = pymysql.connect(
        #     '127.0.0.1', 'root', '123456', 'maoyandb', charset='utf8'
        # )
        # self.cursor = self.db.cursor()
        # self.r = redis.Redis()

    # 获取html函数(因为两个页面都需要发请求)
    def get_page(self, url):
        req = request.Request(
            url=url,
            headers={'User-Agent': UserAgent().random}
        )
        res = request.urlopen(req)
        # ignore参数,实在处理不了的编码错误忽略
        # 查看网页源码,发现网页编码为 gb2312,不是 utf-8
        html = res.read().decode('gbk', 'ignore')
        return html

    # 解析提取数据(把名称和下载链接一次性拿到)
    # html为一级页面响应内容
    def parse_page(self, html):
        # 1. 先解析一级页面(电影名称 和 详情链接)
        pattern = re.compile(
            '<table width="100%".*?<td height="26">.*?<a href="(.*?)".*?>(.*?)</a>', re.S)
        # film_list: [('详情链接','名称'),()]
        film_list = pattern.findall(html)
        # print(film_list)
        # ins = 'insert into filmsky values(%s,%s)'
        print('开始分析')
        string = ''
        for film in film_list:
            film_name = film[1]
            film_link = 'https://www.dytt8.net' + film[0]
            # 2. 拿到详情链接后,再去获取详情链接html,提取下载链接
            while True:
                try:
                    download_link = self.parse_two_html(film_link)
                    download_link = self.pyjs.call(
                        'ThunderEncode', download_link)

                    break
                except Exception as e:
                    continue
            # self.cursor.execute(ins, [film_name, film_link])
            # self.db.commit()
            # 增加到字符串
            string += '电影名称' + film_name + '下载链接' + download_link + '\n'
        return string

    # 解析二级页面,获取下载链接
    def parse_two_html(self, film_link):
        two_html = self.get_page(film_link)
        pattern = re.compile('<td style="WORD-WRAP.*?>.*?>(.*?)</a>', re.S)
        download_link = pattern.findall(two_html)[0]
        print('详情页分析完成')
        return download_link

    # 主函数
    def main(self):
        with open('dianyingtiantang_xunlei_base64.js') as f:
            js = f.read()
        self.pyjs = execjs.compile(js)
        for page in range(2, 3):
            url = self.url.format(page)
            html = self.get_page(url)
            print('第一页下载完成')
            string = self.parse_page(html)
            print('开始写入文件')
            with open('电影天堂电影数据爬取第%s页.txt' % page, 'w') as f:
                f.write(string)
            print('第%d页完成' % page)
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    start = time.time()
    spider = FilmSky()
    spider.main()
    end = time.time()
    print('执行时间:%.2f' % (end - start))
