import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import random

'''
西拉代理，IP爬取=============================================================
'''

# 获取User-Agent


def get_random_ua():
    # 1.创建User-Agent对象
    ua = UserAgent()

    return ua.random


base_url = 'http://www.xiladaili.com/gaoni/{}/'

# 获取所有代理IP的地址和端口号
# [{'http':'http://xxxx:xx','https':'https://xxxx:xxx'},]


def get_ip_list(url):
    # 获取
    headers = {'User-Agent': get_random_ua()}
    # proxies = {
    #     'http': 'http://182.35.81.10:9999',
    #     'https': 'https://182.35.81.10:9999'
    # }
    html = requests.get(url, headers=headers).text
    # 假设自己ip被封，使用代理ip
    # html = requests.get(url, proxies=proxies,headers=headers).text
    # 解析
    parse_html = etree.HTML(html)
    # r_list: [<element tr at xxx>,<element tr at xxx>]
    r_list = parse_html.xpath('//tr')
    # 空列表,存放所有ip和port
    proxy_list = []
    # 依次遍历
    for r in r_list[1:]:
        # print('r.xpath', r.xpath('./td[1]/text()'))
        ip_port = r.xpath('./td[1]/text()')[0]
        # print(ip_port)
        proxy_list.append(
            {
                'http': 'http://{}'.format(ip_port),
                'https': 'https://{}'.format(ip_port)
            }
        )
        # proxy_list: [{}, {}, {}, {}]
    # print(proxy_list)
    return proxy_list

# 测试代理,建立代理IP池


def proxy_pool():
    for x in range(1, 100):
        print('爬取第%s页' % x)
        url = base_url.format(x)
        # 调用上面函数
        proxy_list = get_ip_list(url)
        # 可用代理IP列表
        useful_proxy = []
        # 测试代理是否可用
        for proxy in proxy_list:
            # proxy: {'http':'http://xxxx:xx'}
            headers = {'User-Agent': get_random_ua()}
            try:
                res = requests.get(
                    url='http://httpbin.org/get',
                    headers=headers,
                    proxies=proxy,
                    timeout=5
                )
                # print(res.text)
                useful_proxy.append(proxy)
                print('可以用', proxy)
                # 拿一个就退出,如果想要多拿几个就在这里改
                return
            except Exception as e:
                # print('{}不能用'.format(proxy))
                continue
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    # get_ip_list()
    proxy_pool()
