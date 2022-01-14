# 爬取新浪微博头条前20页

import requests,pymysql
from lxml import etree

def get_element(i):
    base_url = 'https://weibo.com/a/aj/transform/loadingmoreunlogin?'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        'Referer': 'https://weibo.com/?category=1760',
        'cookie': 'Hm_lvt_3eec0b7da6548cf07db3bc477ea905ee=1634802814; runoob-uuid=20047af5-48e3-4ccf-8d8e-95f953ffc8f1; _ga=GA1.2.1036505620.1635125348; __gads=ID=f7904b18f7b4c93c-22a521e7e7cc0096:T=1635232406:RT=1635232406:S=ALNI_MYQhrxzNHQWJYpE4RU74BC6--EPXQ; _gid=GA1.2.21055588.1641882522; _gat_gtag_UA_84264393_2=1',
    }
    params = {
        'ajwvr': '6',
        'category': '1760',
        'page': i,
        'lefnav': '0',
        'cursor': '',
        '__rnd': '1573735870072',
    }
    response = requests.get(base_url,headers=headers,params=params)
    response.encoding = 'utf-8'
    info = response.json()
    return etree.HTML(info['data'])

def connect_mysql(title, time, author, url):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='py_sp_test')
    cursor = db.cursor()
    sql = 'insert into sina_news(title,send_time,author,url) values("' + title + '","' + time + '","' + author + '","' + url + '")'
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def main():
    for i in range(1,20):
        html = get_element(i)
        title = html.xpath('//a[@class="S_txt1"]/text()')
        author_time = html.xpath('//span[@class]/text()')
        author = [author_time[i] for i in range(len(author_time)) if i % 2 == 0]
        time = [author_time[i] for i in range(len(author_time)) if i % 2 == 1]
        url = html.xpath('//a[@class="S_txt1"]/@href')
        for j,tit in enumerate(title):
            title1 = tit
            time1 = time[j]
            url1 = url[j]
            author1 = author[j]
            # print(title1,url1,time1,author1)
            connect_mysql(title1, time1, author1, url1)

if __name__ == '__main__':
    main()














