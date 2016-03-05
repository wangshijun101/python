#!/usr/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing

import time,random

import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid == 0 :
	print 'I am child process (%s) and my parent is %s.' %(os.getpid(),os.getppid())
else:
	print 'I (%s) just created a child process(%s). ' %(os.getpid(),pid)


def long_time_task(name):
	print 'Run task %s (%s)...' %(name, os.getpid())
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print 'Task %s runs %0.2f senconds .' %(name, (end - start))
if __name__ == '__main__':
	print ' parent process %s' %os.getpid()
	p = multiprocessing.Pool()
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print 'Waiting for all subProcesses done...'
	p.close()
	p.join()
	print 'All subprocesses done.'

