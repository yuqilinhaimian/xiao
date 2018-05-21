import os

a = os.fork()
if a<0:
	print("fork调用失败。")
elif a == 0:
	print("我是子进程（%s），我的父进程是（%s）"%(os.getpid(),os.getppid()))
else:
	print("我是父进程（%s），我的子进程是（%s）"%(os.getpid(),a))

print("12313131")