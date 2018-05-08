'''
for i in range(1,10):
	for j in range(1,i+1):
		print('%d*%d=%d'%(j,i,i*j),end = " ")
	print(" ")

i = 0
j = 0
while i < 9:
	i+=1
	while j < 9:
		j+=1
		print(j, "*",i,"=",i*j,end = " ")
		if i == j:
			j = 0
			print(' ')
			break
'''
