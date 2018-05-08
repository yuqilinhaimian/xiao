Account = 123456
Pwd = 123456
i = 1
while True:
	my_Account = int(input('请输入账号：'))
	my_Pwd = int(input('请输入密码：'))
	if Account == my_Account and Pwd == my_Pwd:
		print('登陆成功')
		choose = int(input('请选择英雄:1.ADC,2.肉，3.法师'))
		if choose == 1:
			print('鲁班大师')
		elif choose == 2:
			print('程咬金')
		elif choose == 3:
			print('王昭君')
		break
	else:
		print('错误%d'%i)
		i += 1
		if i == 4:
			print('账号冻结')
			break
