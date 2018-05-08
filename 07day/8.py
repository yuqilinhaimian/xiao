Account = 1
Pwd = 2
nomey = 10000

MyAccount = int(input('请输入账号：'))
MyPwd = int(input('请输入密码：'))

if MyAccount == Account and MyPwd == Pwd:
	print('登录成功')
	out_nomey = int(input('请输入您要取走的金额：'))
	if out_nomey > nomey:
		print('没钱取毛')
	elif out_nomey < nomey:
		print('剩余')
		print(nomey - out_nomey)
else:
	print('非法操作')