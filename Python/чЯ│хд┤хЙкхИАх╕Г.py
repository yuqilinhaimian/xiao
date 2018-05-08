
import random
guess_list = ["石头","剪刀","布"]
guize = [["布","石头"],["石头","剪刀"],["剪刀","布"]]
A = 0
while A < 10:
	computer = random.choice(guess_list)
	people = input("请输入：石头，剪刀，布，\n")
	if people not in guess_list:
		people = input("请重新输入：石头，剪刀，布\n")
		continue
	if computer == people:
		print("平局")
	elif[computer,people] in guize:
		print("你输了")
	else:
		print("你赢了")
		break
	A += 1



















