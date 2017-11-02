#coding=utf-8
'''
1.文件概念
	在Linux中一切皆文件
2.文件打开方式
	open(name[,mode[buf]])
	name 文件路径
	mode 打开方式 (r w a r+ w+ a+)[b]
	buf 缓存buffering大小
3.文件读写操作
	文件读取方式
	read([size]):读取文件(读取size个字节，默认读取全部)
	readline([size]):读取一行，size表示读取一行中的前几个字节
	readlines([size])：读取buffering，返回每一行所组成的列表
	iter			使用迭代器读取文件
	文件写入方式
	write(str):将字符串写入文件
	writelines(sequence_of_strings):写入多行到文件

4.文件指针
5.文件对象属性

6.Linux文件系统
8.os模块文件操作
'''

#读取操作
#迭代器
f=open('pythontest')
iter_f=iter(f)
lines=0
for line in iter_f:
	lines+=1
	# print(line)
print(lines)
f.close()

#写入操作,关闭之后才会写入到文件，因为涉及到文件缓冲机制
#解决方案
#1.主动调用close()或者flush方法，写缓存同步到磁盘
#2.写入数据量大于或者等于写缓存，写缓存同步到磁盘
f=open('pythontest2','w')
f.write('hello pythontest2')
f.flush()
f.close()

# f=open('pythontest2','w')
# # f.writelines(123456)      #必须是字符串序列
# f.writelines(['1','2','3'])
# f.close()

#文件的关闭
'''
1.将写缓存同步到磁盘
2.Linux系统中每个进程打开文件的个数是有限的
3.如果打开文件数到了系统限制，在打开文件就会失败

查看进程限制数
cat /proc/进程ID/limits    fileno 文件对象属性每次打开+1
'''
def test_open_file_limits():
	list_f=[]
	for x in range(1025):
		list_f.append(open('pythontest2','w'))
		print('%d:%d' %(x,list_f[x].fileno()))

# test_open_file_limits()   #打开太多会报错


#python读取和写入的问题
#文件指针
'''
问题1：每次写文件后，必须重新打开才能读取文件
问题2：读取文件后，无法重新读取读过的内容

文件指针操作:
seek(offset[,whence])  :移动文件指针
	offset:偏移量，可以为负数
	whence:偏移相对位置

文件指针定位方式:
os.SEEk_SET		相对于文件起始位置
os.SEEK_CUR 	相对于文件当前位置
os.SEEK_END		相对文件结束位置

f.tell()
f.seek(int,os....)
'''

#文件对象的属性
'''
file.fileno()   文件描述符
file.mode		文件打开权限
file.encoding	文件编码格式
file.closed		文件是否关闭
'''

#标准文件
'''
文件标准输入:sys.stdin
文件标准输出:sys.stdout
文本标准错误:sys.stderr
'''
#文件命令行参数
import sys
if __name__ == '__main__':
	print len(sys.argv)
	for arg in sys.argv:
		print arg

#文件的编码格式
# u'自由的雪'  #无法写入Unicode字符，先转换为utf-8,然后写入到文件
a=unicode.encode(u'自由的雪','utf-8')
print(a)


#问题：如何创建指定编码格式的文件
#使用codecs模块提供方法创建指定编码格式文件
# open(fname,mode,encoding,errors,buffering)


#os模块
'''
os.open(filename,flag[,mode])
flag:打开文件方式
	os.O_CREAT：创建文件
	os.O_RDONLY:只读方式打开
	os.O_WRONLY:只写方式打开
	os.O_RDWR：读写方式打开

os.read(fd,buffersize):读取文件
os.write(fd,string):写入文件 返回写入大小
os.lseek(fd,pos,how):文件指针操作
os.close(fd):关闭文件
'''

#文件练习
'''
int配置文件格式
节:			[session]
参数(键=值)  name=value
'''
import ConfigParser
cfg=ConfigParser.ConfigParser()  #生成ConfigParser对象
cfg.read('python.ini')			 #读取配置文件
cfg.sections()					 #读取节的值[],并返回一个list

def display(cfg):
	for se in cfg.sections():
		print(se)
		print(cfg.items(se)) #迭代节中的内容

display(cfg)
cfg.set('userinfo','pwd','123456')
display(cfg)
cfg.set('userinfo','email','skysnow2017@gmail.com')
display(cfg)
cfg.remove_option('userinfo','email')
display(cfg)


