import requests

import time


def dowmloader(url, path):
    start = time.time()  # 开始时间
    size = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    response = requests.get(url, headers=headers, stream=True)
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 总大小
    print(content_size)
    if response.status_code == 200:
        print('[文件大小]:%0.2f MB' %
              (content_size / chunk_size / 1024))  # 换算单位并打印
        with open(path, 'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)  # 已下载文件大小
                #\r指定行的第一个字符开始，搭配end属性完成覆盖进度条
                print('\r' + '[下载进度]：%s%.2f%%' % ('>' * int(size * 50 /
                                                            content_size), float(size / content_size * 100)), end='')
    end = time.time()  # 结束时间
    print('\n' + '全部下载时间：用时%.2f秒' % (end - start))


url = 'https://upos-hz-mirrorks3u.acgvideo.com/dspxcode/m190725ws2w5nmvlqas8w8362qwa2p2j-1-56.mp4?deadline=1564043851&gen=dsp&wsTime=1564043851&os=ks3u&drate=500000&platform=html5&uparams=deadline,gen,wsTime,os,drate,platform&upsig=c43e089cc085afb15db46ed3b9a6d31c&uuid=5d394e2b89530'
path = 'dd'
dowmloader(url, path)
