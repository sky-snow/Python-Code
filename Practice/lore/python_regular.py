#coding=utf-8

'''
1.正则表达式的基本概念 
	1.使用单个字符串来描述匹配一系列符合某个句法规则的字符串
	2.是对字符串操作的一种逻辑公式
	3.应用场景:处理文本好数据
	4.匹配过程:依次拿出表达式和文本中的字符比较。
2.Python正则表达式的re module
	r'sky'-->Pattern-->Match-->result
3.正则表达式的语法
4.re模块相关方法使用
1.search(pattern,string,flags=0)  在一个字符串中查找匹配
2.findall(pattern,string,flags=0)	找到匹配，返回所有匹配部分的列表
3.sub(pattern,repl,string,count=0,flags=0) 将字符串中匹配的正则表达式的部分替换为其他值
4.split(pattern,string,maxsplit=0,flags=0) 根据匹配分割字符串，返回分割字符串组成的列表
'''
#为什么使用正则表达式
def find_start_with_sky(filename):
	with open(filename) as f:
		for line in f:
			if line.startswith('sky'):
				print(line)

def find_start_with_sky_end_snow(filename):
	with open(filename) as f:
		for line in f:
			# if line.startswith('sky') and line.endswith('snow\n'):
			if line.startswith('sky') and line[:-1].endswith('snow'):
				print(line)

# find_start_with_sky('pythontest')
# find_start_with_sky_end_snow('pythontest')

import re
str1='skysnow python'
print(str1.find('sky'))
print(str1.startswith('sky'))
#生成pattern的实例 使用re.compile的方法,其中r代表原生字符串,
pa=re.compile(r'sky')
print(pa.match(str1))
ma=pa.match(str1)
#返回匹配到的结果
print(ma.group())
#执行匹配,返回tuple下标
print(ma.span())
#查看匹配的字符串
print(ma.string)
#获得匹配的实例
print(ma.re)
#忽略大小写,re.I I代表ignore
pa=re.compile(r'sky',re.I)
print(pa)
ma=pa.match('Skysnow')
print(ma.group())

pa=re.compile(r'[1-9]?[0-9]')
ma=re.match(r'\A[1-9]?\d$','09')
print(ma)
# re.match的对象是临时的，而patter的对象是永久的
'''
字符串匹配
.					匹配任意字符
[...]				中括号匹配其中的任意一个
\d / \D 			匹配数字/非数字
\s / \S 			匹配空白/非空白字符
\w / \W 			匹配单词字符[a-zA-Z0-9]/非单词字符
*					匹配前一个字符0次或者多次
+					匹配前一个字符一次或多次
?					匹配前一个字符0次或者1次
{m} / {m,n}			匹配前一个字符m次或者m到n次
*? /+ /??			匹配模式变为非贪婪
边界匹配
^					匹配字符串开头
$					匹配字符串的结尾
\A / \Z 			指定字符串必须出现在开头/结尾
分组匹配
|					匹配左右任意一个表达式
(ab)				括号中的表达式作为分组
\<number>			引用编号为num的分组匹配到的字符串,匹配XML
(?P<name>)			分组起一个别名
(?P=name)			引用别名为name的分组匹配字符串
'''
ma=re.match(r'[\w]{4,6}@(163|126).com','snow@163.com')
print ma
#匹配XML
ma=re.match(r'<([\w]+>)[\w]+</\1','<book>python</book>')
print ma.group()
#分组的别名与引用
ma=re.match(r'<(?P<sky>[\w]+>)[\w]+</(?P=sky)','<book>python</book>')
print(ma.group())


def add1(match):
	val=match.group()
	num=int(val)+1
	return str(num)
str2='skysnow 2017 1994'
print(re.sub(r'\d+',add1,str2))


import urllib2,re
req=urllib2.urlopen('http://www.imooc.com/course/list')
buf=req.read()
# print(buf)

# listurl=re.findall(r'img[\d]+.+\.jpg',buf)
listurl=re.findall(r'src=.+\.jpg',buf)
listurl=re.findall(r'img[\d]+.+\.jpg',str(listurl))
print(listurl)
# def sub_src(match):
# 	val=match.group()
# 	lst=val[7:]
# 	return lst
listurl=['src="//img.mukewang.com/59eebe270001685606000338-240-135.jpg', 'src="//img2.mukewang.com/59df4dd500013d0606000338-240-135.jpg', 'src="//img2.mukewang.com/59e80cd60001341b06000338-240-135.jpg', 'src="//img1.mukewang.com/59c3917900011b8106000338-240-135.jpg', 'src="//img.mukewang.com/59e716e2000167dc06000338-240-135.jpg', 'src="//img1.mukewang.com/59e5d8fa0001265206000338-240-135.jpg', 'src="//img4.mukewang.com/59df1d83000141a306000338-240-135.jpg', 'src="//img.mukewang.com/5981a729000188dc06000338-240-135.jpg', 'src="//img1.mukewang.com/59dc2a180001f0a112010679-240-135.jpg', 'src="//img1.mukewang.com/59cefd4c0001633206000338-240-135.jpg', 'src="//img.mukewang.com/59c360de0001fefe06000338-240-135.jpg', 'src="//img3.mukewang.com/59c1c80e000193e606000338-240-135.jpg', 'src="//img1.mukewang.com/59c206f500011c4006000338-240-135.jpg', 'src="//img1.mukewang.com/59c32b540001f16f06000338-240-135.jpg', 'src="//img.mukewang.com/59bfab740001369a06000338-240-135.jpg', 'src="//img3.mukewang.com/59c083ed0001245e06000338-240-135.jpg', 'src="//img2.mukewang.com/59ba4b200001468906000338-240-135.jpg', 'src="//img4.mukewang.com/59b77bac0001985906000338-240-135.jpg', 'src="//img4.mukewang.com/597e973600011a6e06000338-240-135.jpg', 'src="//img4.mukewang.com/59ae0e2a0001307706000338-240-135.jpg', 'src="//img4.mukewang.com/59acb1650001adce06000338-240-135.jpg', 'src="//img4.mukewang.com/599150070001993506000338-240-135.jpg', 'src="//img1.mukewang.com/59af678e00017c3b06000338-240-135.jpg']

def download(listurl):
	for url in listurl:
		f=open(str(i)+'.jpg','w')
		req=urllib2.urlopen(url)
		buf=req.read()
		f.write(buf)
		i+=1


