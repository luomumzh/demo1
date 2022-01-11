#爬取新浪新闻指定搜索内容

import requests
import urllib3

urllib3.disable_warnings()
base_url = 'https://search.sina.com.cn/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
} #F12,network拿到请求头
key = '玲娜贝儿' #玲娜贝儿过分可爱
params = {
    'q': key,
    'c':'news',
    'from': 'channel',
    'ie': 'utf_8',
}
response = requests.get(base_url,headers=headers,params=params,verify=False)
with open('sina_news.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

