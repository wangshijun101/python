#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Animal(object):
	def run(self):
		print 'Animal is running'
class Dog(Animal):
	def run(self):
		print 'Dog is running'
class Cat(Animal):
	pass

dog = Dog()
dog.run()
cat = Cat()
cat.run()

class Labulado(Dog):
	def run(self):
		super(Labulado,self).run()
ll = Labulado()
ll.run()

class Student(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value< 0 or value >100:
			raise ValueError('score must between 0 ~100 ')
		self._score = value

s = Student()
s.score = 99

#s.score = 9999

print dir(s)
