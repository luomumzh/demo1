###爬虫学习20例
#### 第一例 爬取百度产品列表
    无问题

#### 第二例 爬取新浪新闻指定搜索内容
    requests报错，需要下载好三个组件，在网络请求后面加上verify=False
    下载超时报错，加-i临时换源，加trust-host信任源
    requests库提示警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate ver，使用urllib3.disable_warnings()

#### 第三例 爬取百度贴吧前十页（get请求）
    params里的参数要了解一下，'pn'是分页
    for循环解决问题

#### 第四例 爬取百度翻译接口
    代码没问题，接口有问题，翻译接口不应该是这样的，出不了结果、

#### 第五例 爬取菜鸟教程的python100例
    





