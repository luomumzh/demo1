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
    
#### 第六例 爬取新浪微博头条前20页
    使用ajax + mysql
    why? base_url = 'https://weibo.com/a/aj/transform/loadingmoreunlogin?'
    host='localhost',user='root',password='123456',database='py_sp_test',table='sina_news'
    公司内网，不敢多下
#### 第七例 爬取搜狗指定图片
    多线程知识的学习
    报错：json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    对多线程有所了解，报错得空解决，先跑下一个
#### 第八例 爬取猫眼电影（使用正则表达式）
    对正则表达式进行复习
    group()报错



