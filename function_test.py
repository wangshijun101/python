#!/usr/bin/env python
# -*- coding:utf-8 -*-
###默认参数必须指向不变对象！
def add_end(L=[]):
	L.append('END')
	return L
print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end([]))
print(add_end())
print(add_end())
def add_end_plus(L=None):
	if L is None:
		L=[]
	L.append('End')
	return L
print(add_end_plus([1,2,3]))
print(add_end_plus(['x','y','z']))
print(add_end_plus([]))
print(add_end_plus())
print(add_end_plus())
###可变参数
def calc(*nums):
	sum = 0
	for n in nums:
		sum = sum + n * n
	return sum
print calc(1,2,3)
nums = [1,2,3]
print calc(*nums)
###关键字参数
def person(name,age,**kw):
	print 'name:' , name,'age:',age,'other:',kw
person('Michael',20)
person('Joseph',20,city = 'beijing')
person('Joseph',20,city = 'beijing',gender='M')
kw = {'city':'Beijing','Job':'Engineer'}
person('Tom',39,**kw)
###在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。可变参数是一个tuple :(x,y,z),关键字参数是一个dict:(x=1,y=2,z=3)
def func(a,b,c=0,*args,**kw):
	print 'a = ',a,'b =',b,'c =',c ,'args= ',args,'kw= ',kw

func(1,2)
func(1,2,c=3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)
args = ('a','b')
kw = {'x':99,'y':100}
func(1,2,3,*args,**kw)
#kw = {'x':99,y:100}
func(1,2,3,*args,**kw)

###递归函数使用尾递归
def fact(n):
	return fact_iter(1,1,n)
def fact_iter(product,count,max):
	if count > max:
		return product
	return fact_iter(product * count, count+1,max)

print fact(3)

###函数作为返回值
###闭包具有极大的威力
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax
def lazy_sum(*args):
	def sum():
		ax = 0 
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1,3,5,6,8)
print f
print f()
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print f1 == f2

def count():
	fs = []
	for i in range(1,4):
	        def f():
	                return i*i
	        fs.append(f)
	return fs
f1,f2,f3 = count()
print f1()
print f2()
print f3()

###匿名函数
print map(lambda x: x*x ,[1,2,3,4,5,6])

def f(x):
	return x * x
print map(f,[1,2,3,4,5,6])
f = lambda x : x * x
print f
print f(5)


###装饰器
def now():
	print '2015-12-24'
f = now
print f.__name__

def log(func):
	def wrapper(*args,**kw):
		print 'call %s():' % func.__name__
		return func(*args,**kw)
	return wrapper
@log
def now():
	print '2015-12-24'
now()

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print '%s %s(): ' % (text, func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print '2015-05-02'
now()
print now.__name__

import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print '%s %s(): ' % (text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator
@log('Execute By copy the properties already')
def now ():
	print '2015-05-02 11:49'

now()
print now.__name__

import functools
def log(*texts):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			if len(texts)== 0:
				print 'Input properties size is zero.'
			else:	
				for text in texts:
					print 'input properties is  %s' %(text)
			print func.__name__
			return func(*args,**kw)
		return wrapper
	return decorator
@log()
def now():
	print '2015-05-02 11:56'
now()

def int2(x,base=2):
	return int(x,base)
print int2('1000000')

kw = {'base' : 2}
print int2('100000',**kw)

###偏函数
max2 = functools.partial(max,10)
print max2(1,3,4,5)

###函数变量作用域
def _private_1(name):
	return 'Hello,%s' % name
def _private_2(name):
	return 'Hi,%s' % name
def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)


