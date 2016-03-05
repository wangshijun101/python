#!/usr/bin/env python
for ch in 'ABC':
	print ch
for index,value in enumerate(['A','B','C']):
	print index,value
for x,y in [(1,1),(2,4),(3,5)]:
	print x,y
L = [x * x for x in range(1,11)]
print L
