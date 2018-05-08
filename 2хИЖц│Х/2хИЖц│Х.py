list = [13,6,10,21,30,50,4,89,2]
def maopao():
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if list[i] > list[j]:
				list[i],list[j], = list[j],list[i]
	print(list)
def erfenfa():
	maopao()
	key = 4
	min = 0
	max = len(list) - 1
	center = int((min+max)/2)
	if key in list:
		while True:
			if list[center] > key:
				center = center - 1
			elif list[center] < key:
				center = center + 1
			elif list[center] == key:
				print(str(key) + "在数组里的第" + str(center) + "个位置")
				break
	else:
		print("没有该数字")

erfenfa()