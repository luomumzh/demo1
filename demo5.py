# 爬取菜鸟教程的python100例

import requests
from lxml import etree
import os

base_url = 'https://www.runoob.com/python/python-exercise-example%s.html'


def get_element(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        'referer': 'https://www.runoob.com/python/python-100-examples.html',
        'cookie': 'Hm_lvt_3eec0b7da6548cf07db3bc477ea905ee=1634802814; runoob-uuid=20047af5-48e3-4ccf-8d8e-95f953ffc8f1; _ga=GA1.2.1036505620.1635125348; __gads=ID=f7904b18f7b4c93c-22a521e7e7cc0096:T=1635232406:RT=1635232406:S=ALNI_MYQhrxzNHQWJYpE4RU74BC6--EPXQ; _gid=GA1.2.21055588.1641882522; _gat_gtag_UA_84264393_2=1',
    }
    response = requests.get(url, headers=headers)
    return etree.HTML(response.text)


def save_element(i, text):
    dirsname = './cainiao/code/'
    if not os.path.exists(dirsname):
        os.makedirs(dirsname)
    with open(dirsname + 'demo5练习实例%s.py' % i, 'w', encoding='utf-8') as fp:
        fp.write(text)


def main():
    for i in range(1, 101):
        html = get_element(base_url % i)
        content = '题目:' + html.xpath('//div[@id="content"]/p[2]/text()')[0] + '\n'
        fenxi = html.xpath('//div[@id="content"]/p[position()>=2]/text()')[0]
        daima = ''.join(html.xpath('//div[@class="hl-main"]/span/text()')) + '\n'
        allin = '"""\n' + content + fenxi + daima + '\n"""'
        save_element(i, allin)
        print(fenxi)


if __name__ == '__main__':
    main()
