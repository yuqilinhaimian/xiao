
adminAccount = "666666"
adminPwd = "666666"
list =[]

#增加图书
def zeng():
	user = {}
	name = input("请输入书名:")
	author = input("请输入作者")
	language = input("请输入语言")
	numder = int(input("请输入书号"))
	user["name"] = name
	user["author"] = author
	user["language"] = language
	user["numder"] = numder
	list.append(user)
#删除图书
def shan():
	name = input("请输入您要删除的名字")
	for i in range(0,len(list)):
		if list[i]["name"] == name:
			list.pop(i)
			break


#修改图书
def gai():
	name = input("请输入您要修改的书名")
	Show = True
	for i in range(0,len(list)):
		if list[i]["name"]  == name:
			tianjiaxinshu(i)
			Show = False
			break
	else:
		if Show:
			print("你输入的书没有记录")

def tianjiaxinshu(position):
	Loop = True
	while Loop:

		mode  = int(input("请输入要修改的信息: 1: 书名 2:作者 3:语言 4:书号 5:退出"))

		if mode == 1:
			name = input("请输入新的书名")
			list[position]["name"] = name
		elif mode == 2:
			author = input("请输入新书作者")
			list[position]["author"] =author
		elif mode == 3:
			language= input("请输入新书语言")
			list[position]["language"] = language
		elif mode == 4:
			numder = input("请输入新书书号")		
			list[position]["numder"] = numder
		elif mode == 5:
			Loop = False



#查询
def cha():
	for i in list:
		print(i)

def Menu():
	while True:
		print("欢迎进入图书管理系统".center(30,"*"))
		print("1:新增图书".center(30,"-"))
		print("2:查询图书".center(30,"-"))
		print("3:修改图书".center(30,"-"))
		print("4:删除图书".center(30,"-"))
		print("5:  退出  ".center(30,"-"))
		mode = int(input("请选择功能序号"))
		if mode == 1:
			zeng()
		elif mode == 2:
			cha()
		elif mode == 3:
			gai()
		elif mode == 4:
			shan()
		elif mode == 5:
			break


def adminLogin():
	account = input("请输入管理员账号:")
	pwd = input("请输入管理员密码:")

	if account != adminAccount or  pwd != adminPwd:
		print("账户或密码错误")

	elif account == adminAccount and pwd == adminPwd:
		print("管理登录成功")
		Menu()


adminLogin()

