
def sushu(year):
		year = int(input("输入年数"))
		if ((year%4 == 0 and year%100 != 0) or year%400 == 0):
			print("%d年是润年"%year)
		else:
			print("%d年是平年"%year)


def month():
	list = [1,13]
	for i in range(list):
		print(i)
