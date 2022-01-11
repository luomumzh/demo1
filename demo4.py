#爬取百度翻译接口

import requests

base_url = 'https://fanyi.baidu.com/sug'
# kw = input('请输入想要翻译的英文单词：')
kw = 'pig'
data = {
    'kw':kw
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'content-length': str(len(data)),
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'referer': 'https://fanyi.baidu.com/',
    'x-requested-with': 'XMLHttpRequest',
}
response = requests.post(base_url, headers=headers,data=data)
print(response.json())

# result = ''
# for i in response.json()['data']:
#     result+=i['v']+'\n'
# print(kw+'的翻译结果为：')
# print(result)

