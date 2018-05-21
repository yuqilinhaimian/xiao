import os
import time

num = 0

pid = os.fork()

if pid == 0:
	time.sleep(5)
	num+=1
	print("dasd%d"%num)
else:
	time.sleep(1)
	num-=1
	print("dasd%d"%num)