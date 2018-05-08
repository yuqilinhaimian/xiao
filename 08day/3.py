i = 0

while i < 5:
	high = int(input("小明身高："))
	weight = float(input("小明体重："))
	BMI = (weight%(high**2))/10
	if BMI < 18.5:
		print("过轻")
	elif BMI >= 18.5 and BMI < 25:
		print("正常")
	elif BMI >= 25 and BMI < 28:
		print("过重")
	elif BMI >= 28 and BMI < 32:
		print("肥胖")
	elif BMI < 32:
		print("过分肥胖")
	i += 1