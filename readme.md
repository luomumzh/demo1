###爬虫学习20例
#### 第一例 爬取百度产品列表
    无问题

#### 第二例 爬取新浪新闻指定搜索内容
    requests报错，需要下载好三个组件，在网络请求后面加上verify=False
    下载超时报错，加-i临时换源，加trust-host信任源
    requests库提示警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate ver，使用urllib3.disable_warnings()

#### 第三例 爬取百度贴吧前十页（get请求）
    





