Account = 666666
pwd = 666666
print("欢迎来到王者荣耀！碾碎他们！")
num = 0
while num < 3:
	myAccount = int(input("请输入帐号:"))
	mypwd = int(input("请输入密码:"))
	if (myAccount == Account) and (mypwd == pwd):
		print("登录成功，请选择位置！")
		hero = int(input("1,ADC\n2,肉\n3,法师\n"))
		if hero == 1:
			print("鲁班")
		elif hero == 2:
			print("成妖精")
		elif hero == 3:
			print("甄姬")
		break
	else:
		print("您输入的帐号或密码错误！")
	num+=1
