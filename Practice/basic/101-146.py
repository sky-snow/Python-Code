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
# 105.编写Python程序，以获得用户的环境
# 106.写Python程序来划分上延伸隔板的路径
# 107.写一个Python程序来检索文件的属性。
# 108.编写Python程序，找出路径指向一个文件或目录，当你遇到一个路径名。
# 109.写一个Python程序来检查，如果数字为正数，负数或零
# 110.编写Python程序了一千五使用匿名函数列表以获得整除的数字
# 111.编写Python程序，使用通配符从当前目录中建立文件列表
# 112.编写一个Python程序，从指定的列表中删除第一个项目。
# 113.写Python程序来输入一个号码，如果它不是一个号码生成的错误消息。
# 114.编写Python程序从列表中筛选正数。
# 115.写Python程序以计算整数列表的产物（不使用用于循环）
# 116.编写Python程序打印Unicode字符。
# 117.写一个Python程序来证明同一值点相同的内存位置的两个字符串变量.
# 118.编写Python程序，从列表中创建一个字节组
# 119.写Python程序，以显示在指定数的浮点数
# 120.编写Python程序来格式化指定的字符串的字符数限制为6
# 121.写Python程序，以确定是否变量被定义或没有。
# 122.编写Python程序空的变量，而不破坏它。
# 123. Write a Python program to determine the largest and smallest integers, longs, floats
# 124.写一个Python程序来检查多个变量具有相同的值。
# 125. Write a Python program to sum of all counts in a collections?
# 126.编写Python程序，以获得实际的模块对象给定对象
# 127.写Python程序，以检查是否一个整数以64位相符。
# 128.编写Python程序，以检查是否在一个字符串存在小写字母。
# 129.编写Python程序，前导零添加到字符串。
# 130.编写Python程序用双引号来显示字符串。
# 131.写Python程序到可变长度字符串分割成变量。
# 132.编写Python程序列出home目录没有绝对路径。
# 133.写Python程序来计算节目的时间运行（启动和当前时间之间的差）
# 134.在单个线写Python程序到输入的两个整数。
# 135.编写Python程序打印的变量，而不值之间的空间
# 136.写一个Python程序来查找文件，并跳过指定目录的目录。
# 137.写Python程序以提取单个键-值对中变量的字典的
# 138.编写Python程序转换成真实的1，假为0 
# 139.编写Python程序无效的IP地址。
# 140.编写Python程序将整数转换成二进制保持前导零。
# 141.编写Python程序，以十进制转换为十六进制
# 142.编写Python程序寻找操作系统的名称，平台和平台的发布日期。
# 143.写Python程序，以确定是否蟒壳在32位或64位模式下操作系统上执行。
# 144.写Python程序，以检查是否变量是整数或字符串的
# 145.编写Python程序寻找操作系统的名称，平台和平台的发布日期。
# 146.编写Python程序找到Python模块源的位置
