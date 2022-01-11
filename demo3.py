#爬取百度贴吧前十页（get请求）

import requests, os

base_url = 'https://tieba.baidu.com/f?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}
dirname = './tieba/woman/'
if not os.path.exists(dirname):
    os.makedirs(dirname)
for i in range(0,10):
    params = {
        'ie':'utf-8',
        'kw':'美女',
        'pn':str(i * 50)
    }
    response = requests.get(base_url, headers=headers, params=params)
    with open(dirname + 'demo3美女第%s页.html'%(i+1),'w',encoding='utf-8') as fp:
        fp.write(response.content.decode('utf-8'))