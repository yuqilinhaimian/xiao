Account = 6666
Pwd = 123
Account1 = int(input('请输入账号：'))
Pwd1 = int(input('请输入密码：'))
while True:
	if Account == Account1 and Pwd ==Pwd1:
		print('登录成功')
		break
	elif  Account != Account1 or Pwd != Pwd1:
		print('您输入的账号或密码错误')
		break
