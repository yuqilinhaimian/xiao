while True:

	i = int(input('请输入一个数字：'))
	j = int(input('请输入一个数字，大于上一个：'))
	sum_1 = 0
	if i < j:
		j += 1
		for k in range(i,j):
			print(k)
			sum_1 = sum_1 + k
		print(sum_1)
		break
	else:
		print('输入错误！')

