#coding=utf-8
#变量
a=3
print a
#基础的四则运算
print 2+5
print 2-5
print 2*5
print 5/2
print '\n'
#输出均为浮点
print 2.0+5
print 2.0-5
print 2.0*5
print 5.0/2
print '\n'
print 2+5.0
print 2-5.0
print 2*5.0
print 5/2.0

#Python解决了整数溢出的问题
print 123456789870987654321122343445567678890098876*1233455667789990099876543332387665443345566

#查看类型函数type()
print type(3.0)

#math库
import math
print dir(math)

print math.sqrt(9)
print abs(-3)


from math import sqrt
for n in range(99, 1, -1):
	root = sqrt(n)
	if root == int(root):
		print n
		break
	else:
		print "Nothing."
