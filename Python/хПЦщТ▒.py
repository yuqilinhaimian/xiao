Account = "123465"
Pwd = "abc"
nomey = 100000
print ("*"*10)
myAccount = input("请输入帐号:")
myPwd = input("请输入密码:")
if myAccount == Account and myPwd == Pwd:
	print("登录成功！")
	mod = int(input("请输入选择功能：1,存2,取"))
	if mod == 1:
		nomey1 = int(input("请输入您要存如的金额:"))

	if mod == 2:
		nomey2 = int(input("请输入您要取出的金额:"))
		if nomey2 <= nomey:
			print("取款成功%d元 剩余%d元"%(nomey,nomey-nomey2))
		else:
			print("余额不足！请及时充值！")
elif myAccount != Account or myPwd != Pwd:
	print("帐号或密码错误！")
else:
	print("系统去火星了")
