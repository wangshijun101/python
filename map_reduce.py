#!/usr/bin/env python

def f(x):
	return x * x
print map(f,[1,2,3,4,5,6,7,8,9])
print map(str,[1,2,3,5,6])

def add(x,y):
	return x + y
print reduce(add , [1,3,5,7])

def fn(x,y):
	return x * 10 + y
print reduce(fn,[1,3,4,7,9])
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}[s]
print reduce(fn,map(char2num,'13579'))

###Excise
def chUp(name):
	return name[0].upper() + name[1:].lower()
print map(chUp,['adam','LiSA','B','a'])

def powerd(num1,num2):
	return num1 * num2
print reduce(powerd,[1,2,3,5])

###Filter
def is_odd(n):
	return n % 2 == 1
print filter(is_odd, [1,2,3,5,6,7,9,10])

def not_empty(s):
	return s and s.strip()
print filter(not_empty,['A','','B',None,'C','  '])

###Sorted
print sorted([2,1,23,46,21,22,23,1002,132])

def reversed_cmp(x,y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0
print sorted([36,3,4,2,4,21,9],reversed_cmp)

L = ['bob','about','zoo','Credit']
print sorted(L)

def cmp_ignore_case(s1,s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	return 0
print sorted(L,cmp_ignore_case)
