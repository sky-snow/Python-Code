# coding=utf-8
# 1.函数作用域LEGB
'''
LEGB  L->E->G->B
L:local函数内部作用域
E:enclosing函数内部与内嵌函数之间 
G:global全局作用域
B:build-in 内置作用域
encloseing就是内层函数__closure__里的值，即内层函数调用外层函数中的变量作为自己的属性
'''

passline = 60  # global

def func(val):
    passline = 90  # local
    print('%x' % id(val))
    if val >= passline:
        print
        'pass'
    else:
        print
        'failed'

    def in_func():
        print
        val  # enclosing val

    in_func()
    return in_func


def Max(val1, val2):
    return max(val1, val2)  # build-in


f = func(89)
f()  # in_func
print(f.__closure__)
print
Max(89, 100)

# 2.闭包理解与使用
'''
闭包概念
Closure:内部函数中对encloseing作用域的变量进行引用
函数实质与属性
1.函数是一个对象
2.函数执行完成后内部变量回收
3.函数属性
4.函数返回值  |产生的变量不会被回收
'''


# passline=60
# def func(val):
# 	print ('%x'%id(val))
# 	if val >= passline:
# 		print 'pass'
# 	else:
# 		print 'failed'

# 	def in_func(): #(val,)
# 		print val  
# 	in_func()
# 	return in_func

# f=func(89)
# f()  #in_func
# print f.__closure__

def func_100(val):
    passline = 60
    if val >= passline:
        print
        'pass'
    else:
        print
        'failed'


def func_150(val):
    passline = 90
    if val >= passline:
        print
        'pass'
    else:
        print
        'failed'


def set_passline(passline):
    def cmp(val):
        if val >= passline:  # encloseing作用域的变量进行引用
            print
            'pass'
        else:
            print
            'failed'

    return cmp


'''
即将函数做为返回对象，内部函数中对encloseing作用域的变量进行引用，
使得encloseing作用域的变量作为属性添加到函数的返回对象当中，进而提高封装与代码复用。
'''
# f_100=set_passline(60)
# f_100(59)


# def my_sum(*arg):
# 	return sum(arg)

# def my_average(*arg):
# 	return sum(arg)/len(arg)

# def dec(func):
# 	def in_dec(*arg): #f
# 		if len(arg)==0:
# 			return 0
# 		for val in arg:
# 			if not isinstance(val,int):
# 				return 0
# 		return func(*arg)
# 	return in_dec

# f=dec(my_sum)  #f=in_dec(*arg)
# print f(1,2,3,4,'2')

# 3.装饰器

'''
1.装饰器用来装饰函数,丰富函数功能
2.返回一个函数对象
3.被装饰器函数标识符指向返回的函数对象
4.语法糖 @deco
'''

'''
高阶函数:
1.接受函数作为参数
2.可以返回函数
3.接受函数，对其进行包装，返回一个新函数
'''


def dec(func):
    print
    'call dec'

    def in_dec(*arg):
        print
        'in dec arg=', arg
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)

    return in_dec


# dec(my_sum)-->得到对象in_deco
# my_sum=in_deco
# my_sum() in_deco() my_sum()
@dec
def my_sum(*arg):
    return sum(arg)


def my_average(*arg):
    return sum(arg) / len(arg)


def deco(func):
    def in_deco(x, y):
        func(x, y)

    return in_deco


# deco(bar)->返回函数对象in_deco
# bar=in_deco  bar对象被作为encloseing变量传递给in_deco作为属性
# bar()执行的是in_deco(),但是在in_deco()中又调用bar()
@deco
def bar(x, y):
    print
    'in bar', x + y
