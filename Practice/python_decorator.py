#coding=utf-8
#1.函数作用域LEGB
'''
LEGB  L->E->G->B
L:local函数内部作用域
E:enclosing函数内部与内嵌函数之间
G:global全局作用域
B:build-in 内置作用域
'''
passline=60   #global

def func(val):
	passline=90    #local
	if val >= passline:
		print 'pass'
	else:
		print 'failed'

	def in_func():
		print val  #enclosing
	in_func()

def Max(val1,val2):
	return max(val1,val2)   #build-in

func(89)
print Max(89,100)
#2.闭包理解与使用
'''
闭包概念
Closure:内部函数中对encloseing作用域的变量进行引用01
函数实质与属性
1.函数是一个对象
2.函数执行完成后内部变量回收
3.函数属性
4.函数返回值

'''

#3.装饰器