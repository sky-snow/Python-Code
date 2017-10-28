#coding=utf-8

# 1.基础概念
#错误：
#	1.语法错误
#	2.逻辑错误
#异常:执行过程中出现问题
#	1.程序遇到逻辑或者算法问题
#	2.计算机异常(内存不够，IO不够)
# 2.常见错误
'''
	NameError  (变量为命名)
	SyntaxError (语法错误)
	IOError		(IO错误)
	ZeroDivisionError (除零)
	ValueError  (强制类型转换)
	KeyboardInterrupt (ctrl+c终止错误)
'''
# 3.异常处理

# a=0
# try:
# 	a
# except NameError as e:
# 	print e
# print 'exec over'

# 运行时异常可以捕获，如果发生语法错误则在执行前就会报错。
#如果异常类型设置的不正确，则也不会捕获到异常

#猜数字游戏

# import random
# num=random.randint(0,100)
# while True:
# 	try:
# 		guess=int(raw_input('Enter 1~100:'))
# 	except ValueError as e:
# 		print 'please enter 1~100!'
# 		continue
# 	if guess>num:
# 		print 'guess bigger',guess
# 	elif guess<num:
# 		print 'guess smaller',guess
# 	else:
# 		print 'Guess OK,Game Over'
# 		break
# 	print '\n'
#多种类型的异常捕获处理结构
# 4.with...as语句与上下文管理
'''
with context[as var]
	with_suite
with语句是用来代替try-except-finally语句的，使代码更加简洁
context表达式是一个对象
var用来保存context返回对象，单个返回值或者元祖
'''

# with open('python') as f:
# 	for line in f.readlines():
# 		print line
'''

1.上下文管理协议:__enter__()与__exit__()
2.上下文管理器
3.进入上下文管理器:调用__enter__()方法，将返回对象返回给as var
4.退出上下文管理器:__exit__()
'''
# class Mycontext(object):
# 	"""docstring for Mycontext"""
# 	def __init__(self, name):
# 		self.name = name

# 	def __enter__(self):
# 		print '__enter__'
# 		return self

# 	def do_self(self):
# 		print 'do_self'
# 		# a

# 	def __exit__(self,exc_type,exc_value,traceback):
# 		print '__exit__'
# 		print 'Error',exc_type,'info',exc_value

# if __name__ == '__main__':
# 	with Mycontext('text context') as f:
# 		print f.name
# 		f.do_self()
'''
with应用场景
1.文件操作
2.进程线程之间互斥对象，例如互斥锁
3.支持上下文的其他对象
'''
# 5.标准异常与自定义异常
# BaseException KeyboardInterrupt Exception SystemExit 
class FileError(IOError):
	pass


try:
	raise FileError,'Test FileError'
except FileError as e:
	print e

class CustomError(Exception):
	def __init__(self,info):
		Exception.__init__(self)
		self.errorinfo=info
		print id(self)

	def __str__(self):
		return self.errorinfo

try:
	raise CustomError('Test CustomError')
	#将异常对象保存到了e这个参数当中
except CustomError as e:
	print e,id(e)

# 6.raise与assert语句
'''
raise主动抛出异常
raise[exception[,args]]
'''
# raise TypeError,'llll'

# assert断言语句
# assert expression [,args]
