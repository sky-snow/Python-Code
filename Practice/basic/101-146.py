#coding=utf-8

# 101.编写Python程序访问和打印URL的内容到控制台,python3支持
# from http.client import HTTPConnection
# def connect_url(url):
# 	conn = HTTPConnection(url)
# 	conn.request("GET", "/")  
# 	result = conn.getresponse()
# 	# retrieves the entire contents.  
# 	contents = result.read() 
# 	print(contents)

# str1='www.baidu.com'

# connect_url(str1)

# 102.编写Python程序获得系统命令的输出
import subprocess
# file and directory listing
# returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
# print("dir command to list file and directory")
# print(returned_text)

# 103.写Python程序从给定的路径中提取的文件名
import os
print(os.path.basename('D:\\GitHub\\Python-Code\\Practice\\basic\\101-146.py'))
# 104.编写Python程序，以获得有效组ID，有效用户ID，实际组ID，当前进程相关联的补充组ID列表
#Linux or unix
# import os
# print("\nEffective group id: ",os.getegid())
# print("Effective user id: ",os.geteuid())
# print("Real group id: ",os.getgid())
# print("List of supplemental group ids: ",os.getgroups())

# 105.编写Python程序，以获得用户的环境
import os
# print(os.environ)

# 106.Write a Python program to divide a path on the extension separator
# import os.path
# for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    # print('"%s" :' % path, os.path.splitext(path))

# 107.写一个Python程序来检索文件的属性。
# import os.path
# import time
# print('File         :', __file__)
# print('Access time  :', time.ctime(os.path.getatime(__file__)))
# print('Modified time:', time.ctime(os.path.getmtime(__file__)))
# print('Change time  :', time.ctime(os.path.getctime(__file__)))
# print('Size         :', os.path.getsize(__file__))

# 108.编写Python程序，找出路径指向一个文件或目录，当你遇到一个路径名
# import os.path
# for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
#     print('File        :', file)
#     print('Absolute    :', os.path.isabs(file))
#     print('Is File?    :', os.path.isfile(file))
#     print('Is Dir?     :', os.path.isdir(file))
#     print('Is Link?    :', os.path.islink(file))
#     print('Exists?     :', os.path.exists(file))
#     print('Link Exists?:', os.path.lexists(file))

# 109.写一个Python程序来检查，如果数字为正数，负数或零
def posi_zero_nega():
	num = float(input("Input a number: "))
	if num > 0:
	   print("It is positive number")
	elif num == 0:
	   print("It is Zero")
	else:
	   print("It is a negative number")
#110.Write a Python program to get numbers divisible by fifteen from a list using an anonymous function
num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)

# 111.编写Python程序，使用通配符从当前目录中建立文件列表
import glob
file_list = glob.glob('*.*')
print(file_list)

# 112.编写一个Python程序，从指定的列表中删除第一个项目。
color = ["Red", "Black", "Green", "White", "Orange"]
print("\nOriginal Color: ",color)
del color[0]
print("After removing the first color: ",color)

# 113.写Python程序来输入一个号码，如果它不是一个号码生成的错误消息。
# while True:
#     try:
#         a = int(input("Input a number: "))
#         break
#     except ValueError:
#         print("\nThis is not a number. Try again...")


# 114.编写Python程序从列表中筛选正数。
nums = [34, 1, 0, -23]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the list: ",new_nums)

# 115.写Python程序以计算整数列表的产物（不使用用于循环）
from functools import reduce
nums = [10, 20, 30,]
nums_product = reduce( (lambda x, y: x * y), nums)
print("Product of the numbers : ",nums_product)

# 116.编写Python程序打印Unicode字符。
# print ord('a')
str = u'\u0050\u0079\u0074\u0068\u006f\u006e\u0045\u0078\u0065\u0072\u0063\u0069 \
\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print(str)

# 117.写一个Python程序来证明同一值点相同的内存位置的两个字符串变量
str1 = "Python"
str2 = "Python"
print("\nMemory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))

# 118.编写Python程序，从列表中创建一个字节组
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
# values = bytearray(nums)  #可变
# values2=bytes(nums)  #不可变
# for x in values: print(x),
# print '\n'
# for x in values2:print(x),
# print '\n'
'''
bytes是byte的序列，而str是unicode的序列。
str 使用encode方法转化为 bytes
bytes通过decode转化为str
bytearray和bytes不一样的地方在于，bytearray是可变的
'''

# 119.写Python程序，以显示在指定数的浮点数
# print float(10)
# 120.编写Python程序来格式化指定的字符串的字符数限制为6
str_num = "1234567890"
print('%.6s' % str_num)
# 121.写Python程序，以确定是否变量被定义或没有。
def whether_define(x,y):
	try:
	  x = 1
	except NameError:
	  print("Variable is not defined....!")
	else:
	  print("Variable is defined.")
	try:
	  y
	except NameError:
	  print("Variable is not defined....!")
	else:
	  print("Variable is defined.")

# whether_define(x,y)

# 122.编写Python程序空的变量，而不破坏它。
n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)()) 
# 123. Write a Python program to determine the largest and smallest integers, longs, floats
# import sys
# print("Float value information: ",sys.float_info)
# print("\nInteger value information: ",sys.int_info)
# print("\nMaximum size of an integer: ",sys.maxsize) 
#可以在Python3中运行

# 124.写一个Python程序来检查多个变量具有相同的值。
x = 20
y = 20
z = 20
if x == y == z == 20:
    print("All variables have same value!")  

# 125. Write a Python program to sum of all counts in a collections?
import collections 
num = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(num).values()))

# dq = collections.deque([1,2,3,4,5])
# dq.rotate(-1) # 左移,1往左移动一位到5后面
# print(dq)

# dic = collections.defaultdict(dict)
# dic['k1'].update({'k2':'aaa'})
# print(dic)

# 126.编写Python程序，以获得实际的模块对象给定对象
from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))

# 127.写Python程序，以检查是否一个整数以64位相符。
# int_val = 30
# if int_val.bit_length() <= 63:
#     print((-2 ** 63).bit_length())
#     print((2 ** 63).bit_length())
	
# 128.编写Python程序，以检查是否在一个字符串存在小写字母。
# str1 = 'A8238i823acdeOUEI'
# print(any(c.islower() for c in str1))

# 129.编写Python程序，前导零添加到字符串。
str1='122.22'
print("Original String: ",str1)
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)

# 130.编写Python程序用双引号来显示字符串。
import json
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))

# 131.写Python程序到可变长度字符串分割成变量。
var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)
var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)

# 132.编写Python程序列出home目录没有绝对路径。
import os.path
print(os.path.expanduser('~'))
# 133.写Python程序来计算节目的时间运行（启动和当前时间之间的差）
from timeit import default_timer
def timer(n):
    start = default_timer()
    # some code here
    for row in range(0,n):
        print(row)
    print(default_timer() - start)

timer(5)
timer(15)

# 134.在单个线程写Python程序到输入的两个整数。
#python3 可运行
# def signle_intput():
# 	print("Input the value of x & y")
# 	x, y = map(int, input().split())
# 	print("The value of x & y are: ",x,y)

# signle_intput()


# 135.Write a Python program to print a variable without spaces between values
x = 30
print('Value of x is "{}"'.format(x))
# 136.写一个Python程序来查找文件，并跳过指定目录的目录。
import os
print([f for f in os.listdir('D:\\GitHub\\Python-Code\\Practice\\basic\\') \
	if os.path.isfile(os.path.join('D:\\GitHub\\Python-Code\\Practice\\basic\\', f))])

# 137.写Python程序以提取单个键-值对中变量的字典的
def get_dict_elem(dic):
	(c1, c2),= dic.items()
	return c1,c2

d = {'Red': 'Green'}
# print get_dict_elem(d)
# 138.编写Python程序转换成真实的1，假为0
def boolean_to_one_or_zero(x):
	return int(x == 'true')

# x = 'true'
# print boolean_to_one_or_zero(x)
# x = 'abcd'
# print boolean_to_one_or_zero(x)

# 139.编写Python程序无效的IP地址。
import socket
addr = '127.0.0.25'
try:
    socket.inet_aton(addr) #用来判断ip是否合法
    print("Valid IP")
except socket.error:
    print("Invalid IP")

# 140.编写Python程序将整数转换成二进制保持前导零。
x=8
# print bin(x).ljust(8,'0')i
# print bin(x).ljust(10,'0')i
print(format(x, '08b'))
print(format(x, '010b'))

# 141.编写Python程序，以十进制转换为十六进制
x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))

# 142.编写Python程序寻找操作系统的名称，平台和平台的发布日期。
import os, platform
print("Operating system name:",os.name)
print("Platform name:",platform.system())
print("Platform release:",platform.release())

# 143.写Python程序，以确定是否蟒壳在32位或64位模式下操作系统上执行。
import struct
print(struct.calcsize("P") * 8)
# 144.写Python程序，以检查是否变量是整数或字符串的
print(isinstance(25,int))
# print isinstance('25',str)
print(isinstance(25,int) or isinstance(25,str))
# print(isinstance([25],int) or isinstance([25],str))
# print(isinstance("25",int) or isinstance("25",str))

# 145.Write a Python program to test if a variable is a list or tuple or a set.
#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
x = ('tuple', False, 3.2, 1)
if type(x) is list:
    print('x is a list')
elif type(x) is set:
    print('x is a set')
elif type(x) is tuple:
    print('x is a tuple')    
else:
    print('Neither a list or a set or a tuple.')

# 146.编写Python程序找到Python模块源的位置
import sys
print("\nList of directories in sys module:")
print(sys.path)
print("\nList of directories in os module:")
import os
print(os.path)


