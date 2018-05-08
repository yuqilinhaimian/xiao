'''
A = 0
price = 2
while A <= 10:
	S = 1
	while S < 2 :
		nomey = S*price
		S += 1
	print(nomey*A)
	A += 1

for i in range(1,10):
	for k in range(1,i+1):
		print("%d*%d=%2d"%(i,k,i*k),end="  ")
	print("")
i = 1
while i <= 9:
	k = 1
	while k <= i:
		print("%d*%d=%2d"%(i,k,i*k),end=" ")
		k+=1


	i+=1
	print("")
'''
i1 = 0
i2 = 0
mysum = 0
for i in range(0,100):
	if i%2 == 0:
		i1+=1
		print("偶数%d"%i1)
	elif i%2 != 0:
		i2+=1
		print("奇数%d"%i2)
mysum = i1+i2
print("和%d"%mysum)
