from threading import Thread
import time


def work1():
	g_num = 0
	for i in range(1000000):
		g_num += 1

	print("%d"%g_num)


def work2():
	g_num = 0
	for i in range(1000000):
		g_num += 1
	print("%d"%g_num)


t1 = Thread(target=work1)
t1.start()

t2 = Thread(target=work2)
t2.start()