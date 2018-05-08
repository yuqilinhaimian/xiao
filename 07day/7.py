Account = 123456
Pwd = 'abc'

MyAccount = int(input('请输入账号:'))
MyPwd = input('请输入密码：')

if MyAccount == Account and MyPwd == Pwd:
	print('登录成功')
elif MyAccount != Account and MyPwd == Pwd:
	print('账号不对')
elif MyAccount == Account and MyPwd != Pwd:
	print('密码不对')