Account = '666666'
Pwd = '666666'
list = []
ID_card_list = []
#增
def add():
	user = {}
	name = input('请输入姓名：')
	ID_card = int(input('请输入身份证号：'))
	telephone_number = int(input('请输入电话号码：'))
	site = input('请输入家庭地址:')
	pwd = int(input('请输入密码：'))
	if ID_card in ID_card_list:
		user['name'] = name
		user['ID_card'] = ID_card
		user['telephone_number'] = telephone_number
		user['site'] = site
		user['pwd'] = pwd
		list.append(user)
		ID_card_list.append(ID_card)
	else:
		print(" ")
#删
def delete():
	name = input('请输入要删除的用户：')
	for i in range(0,len(list)):
		if list[i]['name'] == name:
			list.pop(i)
			break
#改
def change():
	name = input('请输入要修改的用户：')
	Show = True
	for i in range(0,len(list)):
		if list[i]['name'] == name:
			add_user(i)
			Show = False
			break
		if Show:
			print('无此用户！')
#增加更改用户
def add_user(position):
	k = True
	while k:
		mode = int(input('请输入要修改的信息：\n1.姓名\n2.身份证号\n3.电话号码\n4.家庭地址\n5.密码\n6.返回上一步\n:'))
		if mode == 1:
			name = input('请输入姓名：')
			list[position]['name'] = name
		elif mode == 2:
			ID_card = int(input('请输入身份证号：'))
			list[position]['ID_card'] = ID_card		
		elif mode == 3:
			telephone_number = int(input('请输入电话号码：'))
			list[position]['telephone_number'] = telephone_number
		elif mode == 4:
			site = input('请输入家庭地址:')
			list[position]['site'] = site
		elif mode == 5:
			pwd = int(input('请输入密码：'))
			list[position]['pwd'] = pwd
		elif mode == 6:
			k = False
#查
def examine():
	name = input('请输入要查找的用户：')
	flag = 0
	count = 0
	for i in list:
		count += 1
		if name == i['name']:
			flag = 1
			break


	if flag == 0:
		print('查无此人！')
	else:
		print('姓名:%s\n身份证号:%s\n电话号码:%s\n家庭地址%s'%(list[count-1]["name"],list[count-1]["ID_card"],list[count-1]["telephone_number"],list[count-1]["site"]))
#菜单
def Menu():
	while True:
		print("欢迎使用银行卡管理理系统".center(30,"*"))
		print("1:创建用户".center(30,"-"))
		print("2:查看用户".center(30,"-"))
		print("3:修改用户".center(30,"-"))
		print("4:删除用户".center(30,"-"))
		print("5:  退出  ".center(30,"-"))
		mode = int(input("请选择功能序号"))
		if mode == 1:
			add()
		elif mode == 2:
			examine()
		elif mode == 3:
			change()
		elif mode == 4:
			delete()
		elif mode == 5:
			break


#登录
def Login():
	Account_user = input('请输入您的账号：')
	Pwd_user = input('请输入密码：')

	if Account_user != Account or Pwd_user != Pwd:
		print('账号或密码错误！')
	elif Account_user == Account or Pwd_user == Pwd:
		print('登录成功')
		Menu()

Login()