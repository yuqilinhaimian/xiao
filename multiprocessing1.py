from multiprocessing import Process
import os

def test(arg):
	for i in range(3):
		print("hahaha%s"%arg)

p = Process(target=test,args=("laowang",))
p.start()

p.join()
print("heiheihei")
