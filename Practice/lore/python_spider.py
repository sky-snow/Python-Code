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
5.网页解析器(BeautifulSoup)
'''

import urllib
#直接请求
response=urllib.urlopen('http://www.baidu.com')

#获取状态码，如果是200表示获取成功
print(response.getcode())

#读取内容
cont=response.read()
print(cont)