def fun(a,b,opt):
	print"a=",a
	print"b=",b
	print"result=",opt(a,b)

fun(1, 2, lambda x,y:x+y)
a = 1
b = 2
result = 3
