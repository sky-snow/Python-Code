#coding=utf-8
#51.写一个Python程序来确定Python程序的分析
import cProfile
def sum():
    print(1+2)

cProfile.run('sum()')

#52.写一个Python程序来打印到stderr
# from __future__ import print_function
# import sys
# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)

# eprint("abc", "efg", "xyz", sep="--")
########################################无法在IDE中执行

#53.编写Python程序访问的环境变量
# import os
# Access all environment variables 
# print('*----------------------------------*')
# print(os.environ)
# print('*----------------------------------*')
# Access a particular environment variable for Linux
# print(os.environ['HOME'])
# print('*----------------------------------*')
# print(os.environ['PATH'])
# print('*----------------------------------*')

#54.写一个Python程序来获取当前用户名
import getpass
print(getpass.getuser())

#55.写一个Python找到本地IP地址使用Python的STDLIB
import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

#56.写一个Python程序来获取控制台窗口的高度和宽度
#-------------------------------------------------------------
# def terminal_size():
#     import fcntl, termios, struct
#     th, tw, hp, wp = struct.unpack('HHHH',
#         fcntl.ioctl(0, termios.TIOCGWINSZ,
#         struct.pack('HHHH', 0, 0, 0, 0)))
#     return tw, th

# print('Number of columns and Rows: ',terminal_size())
#-------------------------------------------------------------
#57.写一个程序获得执行时间Python的方法
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

#58.编写Python程序，计算前n个正整数
def sum_of_n():
	n = int(input("Input a number: "))
	return (n * (n + 1)) / 2
# print(sum_of_n())

#59.写Python程序转换高度（英尺和英寸）到厘米
def foot_inch_to_cm():
	print("Input your height: ")
	h_ft = int(input("Feet: "))
	h_inch = int(input("Inches: "))
	h_inch += h_ft * 12
	h_cm = round(h_inch * 2.54, 1)
	return h_cm

# print foot_inch_to_cm()

#60.写Python程序来计算直角三角形的斜边。
import math
def calc_hypotenuse(a,b):
	return math.sqrt(a**2+b**2)

print calc_hypotenuse(1,1)
	
#61.写一个Python程序（英尺）的距离换算成英寸，码和英里
def Feet_translate():
	d_ft = int(input("Input distance in feet: "))
	d_inches = d_ft * 12
	d_yards = d_ft / 3.0
	d_miles = d_ft / 5280.0
	return d_inches,d_yards,d_miles

# print(Feet_translate())

#62.写Python程序的时间各单位转换成秒
def time_of_translate():
	days = int(input("Input days: ")) * 3600 * 24
	hours = int(input("Input hours: ")) * 3600
	minutes = int(input("Input minutes: ")) * 60
	seconds = int(input("Input seconds: "))
	time = days + hours + minutes + seconds
	return "The amounts of seconds",time

# print time_of_translate()

#63.写一个Python程序来获得一个绝对的文件路径
import os
def abs_file_path(filename):
	return os.path.abspath(filename)
print abs_file_path('python')
#64.写一个Python程序来获得文件的创建和修改日期/时间
import os.path,time
def get_file_ctime_and_mtime(filename):
	ctime=time.ctime(os.path.getctime(filename))
	mtime=time.ctime(os.path.getmtime(filename))
	return ctime,mtime
print get_file_ctime_and_mtime('python')

#65.写一个Python程序来秒转换为天，小时，分钟和秒
def seconds_to_time():
	time = float(input("Input time in seconds: "))
	day = time / (24 * 3600)
	time = time % (24 * 3600)
	hour = time / 3600
	time %= 3600
	minutes = time / 60
	time %= 60
	seconds = time
	print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

# seconds_to_time()

#66.写一个Python程序来计算身体质量指数
def body_health():
	height = float(input("Input your height in meters: "))
	weight = float(input("Input your weight in kilogram: "))
	print("Your body mass index is: ", round(weight / (height * height), 2))

# body_health()

#67.写Python程序将压力转换以千帕至磅每平方英寸，汞的毫米（毫米汞柱）和大气压力
# kpa = float(input("Input pressure in in kilopascals> "))
# psi = kpa / 6.89475729
# mmhg = kpa * 760 / 101.325
# atm = kpa / 101.325
# print("The pressure in pounds per square inch: %.2f psi"  % (psi))
# print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
# print("Atmosphere pressure: %.2f atm." % (atm))

#68.写Python程序来计算的整数的数字的总和。
def number_in_sum():
	num = int(input("Input a four digit numbers: "))
	result=0
	while num/10 != 0:
		result+=num%10
		num=num/10
	result=result+num
	return result
	# x  = num /1000
	# x1 = (num - x*1000)/100
	# x2 = (num - x*1000 - x1*100)/10
	# x3 = num - x*1000 - x1*100 - x2*10
	# print("The sum of digits in the number is", x+x1+x2+x3)

# print number_in_sum()

#69.写Python程序的三个整数，而无需使用条件语句和循环排序。
def sort_three_numbers():
	x = int(input("Input first number: "))
	y = int(input("Input second number: "))
	z = int(input("Input third number: "))
	a1 = min(x, y, z)
	a3 = max(x, y, z)
	a2 = (x + y + z) - a1 - a3
	return a1,a2,a3

# print sort_three_numbers()

#70.写Python程序按日期排序文件
# import glob
# import os
# files = glob.glob("*.py")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))

#71.写一个Python程序来获得一个目录列表，按创建日期排序
# from stat import S_ISREG, ST_CTIME, ST_MODE
# import os, sys, time

# #Relative or absolute path to the directory
# dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

# #all entries in the directory w/ stats
# data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
# data = ((os.stat(path), path) for path in data)

# # regular files, insert creation date
# data = ((stat[ST_CTIME], path)
#            for stat, path in data if S_ISREG(stat[ST_MODE]))

# for cdate, path in sorted(data):
#     print(time.ctime(cdate), os.path.basename(path))
	
#72.写一个Python程序来获得数学模块的细节
# Imports the math module
import math            
#Sets everything to a list of math module
math_ls = dir(math) # 
print(math_ls)

#73.写一个Python程序来计算线路的中点
def calc_distance_with_two_point():
	print('\nCalculate the midpoint of a line :')

	x1 = float(input('The value of x (the first endpoint) '))
	y1 = float(input('The value of y (the first endpoint) '))

	x2 = float(input('The value of x (the first endpoint) '))
	y2 = float(input('The value of y (the first endpoint) '))

	x_m_point = (x1 + x2)/2
	y_m_point = (y1 + y2)/2
	print("The midpoint of line is :")
	print( "The midpoint's x value is: ",x_m_point)
	print( "The midpoint's y value is: ",y_m_point)

#74.写Python程序哈希一个字
def hash_bit():
	soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
	word=raw_input("Input the word be hashed: ")
	word=word.upper()
	coded=word[0]
	for a in word[1:len(word)]:
		i=65-ord(a)
    	coded=coded+str(soundex[i])
	return coded	

# print hash_bit()

#75.写一个Python程序来获取版权信息
import sys
print("\nPython Copyright Information")
print(sys.copyright)

#76.编写一个Python程序，以获取传递给脚本的命令行参数（脚本的名称，参数的个数，参数）
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

#77.编写一个Python程序来测试系统是一个大端平台还是小端平台
import sys
def judge_little_or_big():
	if sys.byteorder == "little":
	    #intel, alpha
	    print("Little-endian platform.")
	else:
	    #motorola, sparc
	    print("Big-endian platform.")

# judge_little_or_big()

#78.写一个Python程序来查找可用的内置模块。
import sys
import textwrap   #文本包装
def find_bif():
	module_name = ', '.join(sorted(sys.builtin_module_names))
	print(textwrap.fill(module_name, width=70))

# find_bif()

#79.写一个Python程序来获得一个物体的大小以字节为单位
import sys
str1 = "one"
str2 = "four"
str3 = "three"
print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
#80.写一个Python程序来获得的递归限制的当前值，即递归层次的限制。
import sys
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())

#81.写一个Python程序来连接N个字符串
def connect_char():
	list_of_colors = ['Red', 'White', 'Black']  
	colors = '-'.join(list_of_colors)
	print("All Colors: "+colors)

# connect_char()

#82.编写一个Python程序来计算一个容器的总和
# s = sum([10,20,30])
# print("\nSum of the cntainer: ",s)

#83.编写一个Python程序来测试某个数字是否大于列表的所有数字
def cmp_other():
	num=input('please a number:')
	lst=range(1,10)
	print(all(num > x for x in lst))

# cmp_other()

#84.编写一个Python程序来计算一个字符串中特定字符的出现次数
def count_char(str,char):
	return str.count(char)

str_test='abcabcabcd'
print count_char(str_test,'d')

#85.编写一个Python程序来检查一个文件路径是一个文件还是一个目录。
import os 
def demo01(filename):  
	if os.path.isdir(filename):  
	    print("\nIt is a directory")  
	elif os.path.isfile(filename):  
	    print("\nIt is a normal file")  
	else:  
	    print("It is a special file (socket, FIFO, device file)" )

# demo01('python')

#86.写一个Python程序来获得一个字符的ASCII值。
def to_ascii(char):
	return ord(char)

# print to_ascii('a')

#87.写一个Python程序来获取文件的大小。
import os
def get_file_size(filename):
	return os.path.getsize(filename)

# print get_file_size('python')

#88.鉴于变量X = 30和y = 20，写一个Python程序打印吨“30 + 20 = 50”
x = 30
y = 20
print("\n%d+%d=%d" % (x, y, x+y))
#89.写Python程序，如果条件为真要执行的操作
n=1
if n == 1:
    print("\nFirst day of a month")

#90.写一个Python程序来创建其自己的源代码的副本
print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())
#91.写一个Python程序来交换两个变量|考虑深拷贝与软拷贝
def swap(a,b):
	a,b=b,a
	return a,b
a=1
b=2
a,b=b,a
print swap(a,b)
print a

#92.写Python程序定义一个包含各种形式的特殊字符的字符串
print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')

#93.写一个Python程序来获取对象的身份
def return_id(obj):
	return id(obj)

#94.写Python程序的字节字符串转换为整数的列表
def str_to_num(str1):
	lst=[]
	for x in str1:
		lst.append(ord(x))
	return lst

# print str_to_num('abc')

#95.写一个Python程序来检查一个字符串是否是数字
str1 = 'a123'
str2 = '123'
def num_or_str(str):
	try:
	    i = float(str)
	except (ValueError, TypeError):
	    print('\nNot numeric')
	else:
		print 'is number'

# num_or_str(str1)
# num_or_str(str2)


#96.写一个Python程序打印当前调用堆栈
import traceback
def f1():
	def abc():
		traceback.print_stack()
	return abc()

print f1()


#97.写Python程序列出的语言中使用的特殊变量。

# s_var_names = sorted((set(globals().keys()) | \
#set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
# print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )

#98.写一个Python程序来获取系统时间。
import time
print(time.ctime())


#99.写Python程序清除屏幕或终端
import os
import time
# for windows
os.system('dir')
time.sleep(2)
os.system('cls')
print '\n'
#for linux
# os.system("ls")
# time.sleep(2)
# # Ubuntu version 10.10
# os.system('clear')

#100.写一个Python程序来获得该程序运行的主机名。
import socket
host_name = socket.gethostname()
print("Host name:", host_name)

