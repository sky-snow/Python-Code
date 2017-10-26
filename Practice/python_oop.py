#coding=utf-8

#1.定义类
#旧式类，不继承object
class OldStyle:
	def __init__(self,name):
		self.name=name
#新式类，继承object，在python3中都是新式类
class NewStyle(object):
	"""docstring for new_style"""
	def __init__(self, arg):
		self.arg = arg
#构造函数
	# def __init__(self,[...]):
#析构函数
	# def __del__(self,[...])
if __name__ == '__main__':
	old=OldStyle('skysnow')
	print old
	print type(old)
	print dir(old)
	print '--------------------------------'
	new=NewStyle(1)
	print new
	print type(new)
	print dir(new)

#定义类的属性
class Programer(object):
	# 1.直接在类下定义，相当于全局，所有类的属性都是一样
	sex='male'
	"""docstring for Programer"""
	# 2.在构造方法定义，每个实例都是不同的||访问控制，通过编程规范
	def __init__(self, name,age,weight):
		self.name = name    #public
		self._age=age      #private
		self.__weight=weight   #部分私有

	def get_weight(self):
		return self.__weight

if __name__ == '__main__':
	programer=Programer('skysnow',25,80)
	print programer.__dict__
	print programer.get_weight()
	print programer._Programer__weight

#定义类的方法,可以看做是类的属性，所以也可以赋值,方法和函数是有区别的，方法是类的一部分。
class Test(object):
	"""docstring for Test"""
	def test(self):
		pass
if __name__ == '__main__':
	a=Test()
	print a.test
	a.test='123'
	print a.test

#关于方法的访问控制，与属性访问控制的语法规范是相同的
#方法的装饰器 @classmethod 直接有类名调用  @property 调用时候不需要加括号
class Programer2(object):
	hobby='basketball'
	def __init__(self, name,age,weight):
		self.name = name    #public
		self._age=age      #private
		self.__weight=weight   #部分私有

	@classmethod
	def get_hobby(cls):
		return cls.hobby

	@property	
	def get_weight(self):
		return self.__weight

	def self_introduction(self):
		print 'My name is %s ,I am %s years old\n' %(self.name,self._age)

if __name__ == '__main__':
	programer=Programer2('skysnow',25,80)
	print dir(programer)
	print Programer2.get_hobby()
	print programer.get_weight
	programer.self_introduction()

#2.类的继承
class Test2(Test):
	"""docstring for Test2"""
	def __init__(self, arg):
		#调用方法使用super()或者使用类名.方法名
		super(Test2, self).__init__()
		# Test.__init__()
		self.arg = arg
#子类的类型判断 使用BIF，isinstance判断类型的与issubclass判断是否是子类。
#Python多继承，实际开发应用较少。

#Python Magic Method
#即方法名前后有俩个下划线的，例如__init__(self)
#对象的创建与初始化的过程
#创建类的对象---------------->初始化对象
#def__new__(cls)              def__init(self)
class Programer3(object):
	def __new__(cls,*args,**kwargs):
		print 'call __new__ Method'
		print args
		return super(Programer3,cls).__new__(cls,*args,**kwargs)

	def __init__(self, name,age):
		print 'call __init__ Method'
		self.name = name    #public
		self._age=age      #private
if __name__ == '__main__':
	programer=Programer3('skysnow',24)
	print programer.__dict__
#回收对象
#__del__()


#类与运算符,可以重写

#比较运算符 
# __cmp__(self,other)  __eq__(self,other) __lt__(self,other) __gt__(self,other)

#数字运算符
# __add__(self,other) __sub__(self,other)  __mul__(self,other) __div__(self,other)

#逻辑运算符
# __or__(self,other) __and__(self,other)

#转换为字符串
# __str__ 适合人理解 __repr__ 适合机器理解 __unicode__


class Programer4(object):
	def __init__(self, name,age):
		self.name = name    #public
		if isinstance(age,int):
			self.age=age      #private
		else:
			raise Exception('age must be int')

#查看注释前后的输出
	# def __str__(self):
	# 	return '%s is %s years old' %(self.name,self.age)


	# def __dir__(self):
	# 	return self.__dict__.keys()

if __name__ == '__main__':
	p=Programer4('skysnow',20)
	print p
	print dir(p)

#类的属性访问，设置对象属性 都需要注意无限递归
def __setattr__(self,name,value):
	self.__dict__[name]=value
#查询对象属性
def __getattr__(self,name):
	pass

def __getattribute__(self):
	pass

#删除对象属性
def __delattr__(self,name):
	pass

class Programer5(object):
	def __init__(self, name,age):
		self.name = name    #public
		if isinstance(age,int):
			self.age=age      #private
		else:
			raise Exception('age must be int')

	def __getattribute__(self,name):
		#前俩中都会引起无限递归
		# return getattr(self,name)
		# return self.__dict__[name]
		return super(Programer5,self).__getattribute__(name)

	def __setattr__(self,name,value):
		#第一种写法会引起无限递归
		# setattr(self,name,value)
		self.__dict__[name]=value

if __name__ == '__main__':
	p=Programer5('skysnow',20)
	print p.name