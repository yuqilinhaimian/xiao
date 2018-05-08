list = []
list_1 = []

i = 0
while i < 3:
	dict = {}
	dict_1 = {}
	name = input('请输入名字:')
	age = int(input('请输入年龄:'))
	sex = input('请输入性别:')
	qq = int(input('请输入qq:'))
	weight = int(input('请输入体重:'))
	dict_1['name'] = name
	if dict_1 in list_1:
		print('名字重复，请重新输入:')
		continue
	list_1.append(dict_1)
	dict['age'] = age
	dict['sex'] = sex
	dict['qq'] = qq
	dict['weight'] = weight
	dict.update(dict_1)
	list.append(dict)
	i += 1

	print(list)
for i in list:
	for k,v in i.items():
		print('%s的是%s'%(k,v))

	
