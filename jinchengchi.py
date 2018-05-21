from multiprocessing import Pool
import os
import random
import time


def wofk(msg):
	print("%s开始执行,进程号为%d"%(msg,os.getpid()))

p=Pool(3)
for i in range(10):
	p.apply(wofk,(i,))

p.close()
p.join()
