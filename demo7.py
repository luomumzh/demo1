# 爬取搜狗指定图片(多线程)

import requests, json, threading, time, os
from queue import Queue


class Picture(threading.Thread):
    def __init__(self, num, search, url_queue = None):
        super().__init__()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        }
        self.num = num
        self.search = search

    def get_url(self):
        url_list = []
        for start in range(self.num):
            url = 'https://pic.sogou.com/pics?query=' + self.search + '&mode=1&start=' + str(
                start * 48) + '&reqType=ajax&reqFrom=result&tn=0'
            url_list.append(url)
        return url_list

    def get_page(self, url):
        response = requests.get(url.format('唯美女孩'), headers=self.headers)
        return response.content.decode('utf-8')

    def run(self):
        while True:
            if url_queue.empty():
                break
            else:
                url = url_queue.get()
                data = json.loads(self.get_page(url))
                try:
                    for i in range(1, 49):
                        pic = data['items'][i]['pic_url']
                        reponse = requests.get(pic)
                        if not os.path.exists(r'D:\spider\picture' + self.search):
                            os.mkdir(r'D:\spider\picture' + self.search)
                        with open(r'D:\spider\picture' + self.search + '/%s.jpg' % (str(time.time()).replace('.', '_')), 'wb') as f:
                            f.write(reponse.content)
                            print('下载成功！')
                except:
                    print('该页图片保存完毕')


if __name__ == '__main__':
    num = int(input('请输入爬取页数（每页48张）：'))
    content = input('请输入爬取内容：')
    pic = Picture(num, content)
    url_list = pic.get_url()
    url_queue = Queue()
    for i in url_list:
        url_queue.put(i)
    crawl = [1, 2, 3, 4, 5]
    for i in crawl:
        pic = Picture(num, content, url_queue=url_queue)
        pic.start()
