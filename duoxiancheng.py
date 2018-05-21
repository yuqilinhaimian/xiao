from threading import Thread
import time


def sing():
	while True:
		time.sleep(1)
		print("唱歌")
def dance():
	while True:
		time.sleep(1)
		print("跳舞")

t1 = Thread(target=sing)
t2 = Thread(target=dance)
t1.start()
t2.start()