#爬取百度产品列表

import requests

baseurl = 'https://www.baidu.com/more/'

response = requests.get(baseurl)

# print(response.text)
# print(response.encoding)

# response.encoding = 'utf-8'
# print(response.text)

with open('index.html','w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(response.status_code)
print(response.headers)
print(type(response.text))
print(type(response.content))
print(response.text)