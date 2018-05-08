'''
print('*'*10,'欢迎使用个人信息管理系统','*'*10)

date = []
while True:
	a = int(input('1.新增\n2.查询\n3.修改\n4.删除'))
	if a==1:
		name = input('请输入名字：')
		age = input('请输入年龄：')
		sex = input('请输入性别：')
		work = input('请输入工作：')
		date.append(name)
		date.append(age)
		date.append(sex)
		date.append(work)
		print(date)
	elif a == 2:
		b = input('请输入要查找的数组')
		print(date[b])
	elif a == 3:
		newname = input('请输入修改的数组')
		date[0] = new
		print(date)
	elif a == 4:
		delname = ('请输入删除的数组')
		del date[0] = delname
		print(date)
		break
'''
list = [["zhaoyuan","nv"],["zhaoyuan","nv"]]
for i in list:
	print(list)
