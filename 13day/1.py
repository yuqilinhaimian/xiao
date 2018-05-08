list = []
def wangzherongyao():




	while True:
		hero = input('请输入一个英雄')
		list.append(hero)
		i = len(list)
		if i == 5:
			print(list)
			break
def jiujiuchengfabiao():
	for i in range(1,10):
		for j in range(1,i+1):
			print('%d*%d=%d'%(j,i,i*j),end = ' ')
		print(' ')
def runnian():
	year = int(input('请输入一个年份'))
	if (year%400 == 0 and year%4 == 0) or year%100 != 0:
		print('runnian')
	else:
		print('pingnian')
'''
def sushu():
	for i in range(100,201):
		if i%i != 0:
			print('素数%d'%i)
sushu()
'''
runnian()
jiujiuchengfabiao()
wangzherongyao()