def a(x,y):
	return x + y
#加
def b(x,y):
	return x - y
#减
def c(x,y):
	return x * y
#成
def d(x,y):
	return x / y
A = 4
while A:
	print('请选择你要如何运算')
	print('1.加')
	print('2.减')
	print('3.成')
	print('4.除')

	choose = input('请输入你要选择的项目：')

	num1 = int(input('输入数字'))
	num2 = int(input('输入数字'))
	if choose == '1':
		print(num1,'+',num2,'=',a(num1,num2))
	elif choose == '2':
		print(num1,'-',num2,'=',b(num1,num2))
	elif choose == '3':
		print(num1,'*',num2,'=',c(num1,num2))
	elif choose == '4':
		print(num1,'/',num2,'=',d(num1,num2))
	else:
		print('输入无效')
