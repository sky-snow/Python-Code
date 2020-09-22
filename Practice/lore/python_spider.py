#coding=utf-8
'''
1.爬虫简介
2.简单爬虫架构
	爬虫调度端->URL管理器->网页下载器->网页解析器
3.url管理器
	管理待抓取和已经抓取的url集合
	--防止重复抓取，循环抓取
	机制与功能:添加新URL到待爬取集合中
			 判断待添加URL是否在容器中
			 获取待爬取URL
			 判断是否有待爬取URL
			 将URL从未爬取移动到已爬取
	实现方式:
		1.内存:python内存--待爬取URL集合:set(),已爬取URL集合:set()
		2.关系数据库:mysql:urls(url,is_crawled)
		3.缓存数据库中:redis:待爬取URL集合:set(),已爬取URL集合:set()
4.网页下载器(urllib2:基础的模块,request:第三方插件，功能强大)
	将互联网上的URL对应的网页下载到本地的工具
	urllib2下载网页的方法:
		1.urlopen(url)
		2.添加data,http header
		3.添加特殊情景的处理器
		    HTTPCookieProcessor:需要账户密码登陆的网站
		    ProxyHandler:需要代理登陆的网站
		    HTTPSHandler:需要https登陆的网站
		    HTTPRedirectHandler:网站内部重定向
		    统一传给urllib2.build_opener(handler)

5.网页解析器(BeautifulSoup)
    1.正则表达式re:模糊匹配
    2.python自带的html.parser 结构化解析
    3.beautifulSoup 结构化解析
    4.lxml  结构化解析
'''

# import urllib2
# #直接请求
# response=urllib2.urlopen('http://www.baidu.com')
#
# #获取状态码，如果是200表示获取成功
# print(response.getcode())
#
# #读取内容
# cont=response.read()
# print(cont)


#创建request对象
# request=urllib2.Requeset(url)
#
# #添加数据
# request.add_data('a','1')
#
# #添加http的header
# request.add_header('User-Agent','Mozilla/5.0')
#
# #发送请求获取结果
# response=urllib2.urlopen(request)

import urllib2,cookielib

#创建cookie容器
cj=cookielib.CookieJar()

#创建一个opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#给urllib2安装opener
urllib2.install_opener(opener)

#使用带有cookie的urllib2访问网页
response=urllib2.urlopen('http://www.baidu.com')

print response.getcode()


#创建BeautifulSoup对象
from bs4 import BeautifulSoup
#根据网页字符串创建BeautifulSoup对象
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup=BeautifulSoup(html_doc,        #HTML文档字符串
                   'html.parser',    #HTML解析器
                   from_encoding='utf8'     #HTML文档的编码
                   )

#搜索节点(find_all,find)
links=soup.find_all('a')
#访问节点信息:以字典的形式访问
for link in links:
    print link.name,link['href'],link.get_text()

#url格式，数据格式，页面编码

'''
扩展:需要登录，验证码，Ajax,服务器防爬虫，多线程，分布式
'''
