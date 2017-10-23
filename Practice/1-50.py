#coding=utf-8

#1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond  the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#2 查看Python版本信息
import sys
print sys.version
print sys.version_info

#3 显示最近时间
import datetime
now=datetime.datetime.now()
print now

#4 接受输入半径，输出面积
# import math
# radius=input('please input radius:')
# print 'area is:',radius*radius*math.pi

#5 输入姓名然后反转
# first_name=raw_input('please input first_name:')
# last_name=raw_input('please input last_name:')
# print last_name,first_name

#------------------------------------------------------------------
#6 接受输入的数字，转换成list and tuple 
# values = input("Input some comma seprated numbers : ")
# ist = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)
# #Python2不能运行
# values = raw_input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)
#------------------------------------------------------------------

#7 输入一个文件名获得后缀名
# filename=raw_input('please input filename:')
# print filename.split('.')[-1]

#8 编写一个Python程序，从下列列表中显示第一个和最后一个颜色
color_list = ['Red','Green','White','Black'] 
print color_list[0::3]

#9.编写一个Python程序来显示考试时间表
exam_st_date=(11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

#10 写接受的整数（n）和计算的n + NN + NNN的值Python程序
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# print n2
# n3 = int( "%s%s%s" % (a,a,a) )
# print n3
# print (n1+n2+n3)

#11 编写一个Python程序来打印Python内置函数的文档
print(abs.__doc__)

#12.编写一个Python程序来打印给定月份和年份的日历
# import calendar
# y=int(input('Input the year:'))
# m=int(input('Input the month:'))
# print calendar.month(y,m)

#13 编写一个Python程序，打印下面这个文档
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#14 编写一个Python程序来计算两个日期之间的天数
from datetime import date
f_date=date(2014,7,2)
l_date=date(2014,7,11)
delta=l_date-f_date
print type(delta)
print delta.days

#15 编写一个Python程序来获取半径为6的球体的体积
import math
r= 6.0
V= 4.0/3.0*math.pi* r**3
print('The volume of the sphere is: ',V)

#16 编写一个Python程序以获得给定数字和17之间的差异，如果数字大于17则返回绝对差异的两倍
# number=input('please input a number:')
# if (number-17)>17 :
# 	print (number-17)*2
# else:
# 	print number-17

#17 .编写一个Python程序来测试一个数字是否在1000或2000之内
def test_number(number):
	return number>1000 and number<2000

print test_number(1001)


#18.编写一个Python程序来计算三个给定数字的总和，如果值相等，则返回三次给定数字的总和
def add(n1,n2,n3):
	if n1==n2 and n2==n3:
		return n1*3*3
	else:
		return n1+n2+n3
print add(1,1,1)

#19 编写一个Python程序以从给定的字符串获取一个新的字符串，其中“Is”已经添加到前面。
#   如果给定的字符串已经以“Is”开始，则返回字符串不变
def new_string(string):
	if len(string)>2 and string[:2]=='ls':
		return string
	else:
		return 'ls'+string

print new_string('aaa')


#20 编写一个Python程序来获取一个给定字符串的n（非负整数）副本的字符串。
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))

#21.编写一个Python程序来查找给定的数字（从用户接受）是偶数还是奇数，打印出适当的消息给用户
# import math
# def odd_or_even():
# 	number=input('please input a number:')
# 	if abs(number)/2!=0:
# 		print 'you input a even.'
# 	else:
# 		print 'you input a odd number.'

# odd_or_even()

#22.编写一个Python程序来统计给定列表中的数字4。
def calc_four(lst):
	return lst.count(4)

lst=[0,2,3,4,4,5,4]
print 'the number of four is:',calc_four(lst)

#23.编写一个Python程序以获取给定字符串的前2个字符的n（非负整数）副本。
#   如果长度小于2 ，则返回整个字符串的n个副本
def sub_string_copy(string,n):
	if len(string)>2:
		return string[:2]*n
	else:
		return string*n

print sub_string_copy('abcb',2)
print sub_string_copy('p',3)


#24.编写一个Python程序来测试一个通过的字母是否是元音。
def judge_vowel(char):
	str='aeiou'
	if char in str:
		return char+' is a vowel.'
	else:
		return char+' is not vowel.'

print judge_vowel('m')

#25.编写一个Python程序来检查一组值中是否包含指定的值.
def is_group_member(group_data, n):
    if n in group_data:
    	return True
    return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))


#26.编写一个Python程序，从给定的整数列表中创建一个直方图.
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])

#27.编写一个Python程序，将列表中的所有元素连接成一个字符串并返回
def connect(lst):
	result=''
	for x in lst:
		result+=str(x)
	return result

print connect([1,2,3,4,'b'])

#28.编写一个Python程序，以相同的顺序从给定的数字列表中打印所有偶数，
#	如果序列中有237个数字，则停止打印.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for x in numbers:
	if x == 248:
		break
	elif x % 2 == 0:
		print(x)

#29.编写一个Python程序，打印出一个包含color_list_1中不存在于color_list_2中的所有颜色的集合
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

def complement(set1,set2):
	union=set1|set2
	result=union-set2
	return result

print complement(color_list_1,color_list_2)
print color_list_1.difference(color_list_2)

#30.写Python程序，将接受一个三角形的底边和高度，并计算面积.
def area():
	base = float(input("Input the base : "))
	height = float(input("Input the height : "))
	return base*height/2
# print area()

def area2(base,height):
	return float(base*height)/2

print area2(1,1)

#31.写一个Python程序来计算两个正整数的最大公约数（GCD）
'''
	辗转相除法：取两个数中最大的数做除数，较小的数做被除数，用最大的数除较小数，
			如果余数为0，则较小数为这两个数的最大公约数，如果余数不为0，
			用较小数除上一步计算出的余数,直到余数为0，则这两个数的最大公约数为上一步的余数。
	相减法：取两个数中的最大的数做减数，较小的数做被减数，用最大的数减去小数，
		如果结果为0，则被减数就是这两个数的最大公约数，如果结果不为0，
		则继续用这两个数中最大的数减较小的数，直到结果为0，则最大公约数为被减数。
	穷举法：将两个数作比较，取较小的数，以这个数为被除数分别和输入的两个数做除法运算，
		被除数每做一次除法运算，值减少1，直到两个运算的余数都为0，
		则该被除数为这两个数的最大公约数。
'''
def gcd1(number1,number2):
	reslut=divmod(max(number1,number2),min(number1,number2))
	if reslut[1]==0:
		return min(number1,number2)
	else:
		return gcd1(reslut[1],min(number1,number2))

print gcd1(20,16)


def gcd2(number1,number2):
	reslut=max(number1,number2)-min(number1,number2)
	if reslut==0:
		return min(number1,number2)
	else:
		return gcd2(reslut,min(number1,number2))

print gcd2(20,16)

def gdc3(number1,number2):
	min_number=min(number1,number2)
	while (number1%min_number)!=0 or (number2%min_number)!=0:
		min_number-=1
	return min_number

print gdc3(20,16)


#32.编写一个Python程序以获得两个正整数的最小公倍数（LCM）
def lcm(number1,number2):
	return number1*number2/gcd1(number1,number2)

print lcm(20,16)

#33.写Python程序，计算三个整数和。但是，如果两个值相等，则和将为零
def sum_zero(a,b,c):
	if a==b or a==c or b==c:
		return 0
	else:
		return a+b+c

print sum_zero(1,2,3)
print sum_zero(1,2,2)

#34.写一个Python程序来概括两个给定整数。然而，如果总和在15到20之间，它将返回20
def sum_to_twenty(a,b):
	# return 20 if a+b>15 and a+b<20 else a+b
	return 20 if a+b in range(15,20) else a+b

print sum_to_twenty(15,4) 

#35.编写一个Python程序，如果两个给定的整数值相等或者它们的总和或差值为5，则返回true。
def function1(a,b):
	if a+b==5 or abs(a-b)==5:
		return True
	else:
		return False

print function1(1,7)

#36.如果两个对象都是整数类型，则编写一个Python程序来添加两个对象
def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Inputs must be integers")
    return a + b

print(add_numbers(10, 20))

#37.写一个Python程序有三种不同的行，以显示您的详细信息，如姓名，年龄，地址.
def personal_details():
    name, age = "skysnow", 24
    address = "shanxi,datong , china"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()
	
#38.写Python程序来解决（X + Y）*（X + Y）
def multiply(x,y):
	return (x+y)**2

print multiply(1,3)


#39.编写一个Python程序来计算指定本金的未来价值，利率和多少年
def interest_rate(amt,rate,years):
	return amt*((1+(0.01*rate)) ** years)

print interest_rate(10000,3.5,7)

#40.写Python程序来计算点之间和(X2，Y2)的距离(X1，Y1).
from math import sqrt
def distance(coordinate1,coordinate2):
	return sqrt(abs(coordinate1[0]-coordinate2[0])**2+abs(coordinate1[1]-coordinate2[1])**2)

a=(0,0)
b=(0,2)
print distance(a,b)

#41.写一个Python程序来检查文件是否存在。
import os
def file_is_exist(filename):
	file=open(filename)
	if file==None:
		return False
	return True

# import os.path
# open('abc.txt', 'w')
# print(os.path.isfile('abc.txt'))
print file_is_exist('python')

#42.编写一个Python程序来确定一个Python shell是否在操作系统上以32位或64位模式执行
import struct
print(struct.calcsize("P") * 8)

#43.写一个Python程序来获得操作系统的名称，平台和发布信息
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())

#44.写一个Python程序来定位的Python站点包
import site; 
print(site.getsitepackages())
#45.写Python程序在Python调用外部命令
# import os
# os.popen('calc')
# os.system('calc')

# from subprocess import call
# call(["ls", "-l"])

#46.写一个Python程序来获得当前正在执行的文件的路径和名称
import os
print("Current File Name : ",os.path.realpath(__file__))

#47.写Python程序，找出CPU的数量使用
import multiprocessing
print(multiprocessing.cpu_count())

#48.写Python程序解析字符串浮动或整数。
n = "246.2458"
print(float(n))
print(int(float(n)))

#49.写Python程序列出Python中的一个目录中的所有文件
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('D:\\hello') if isfile(join('D:\\hello', f))]
print(files_list);

#50.写Python程序无需换行或空间来打印。
for x in xrange(0,10):
	print('*'),

	

	

	
	





























