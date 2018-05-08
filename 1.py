class car():
	def move(self):
		print("车在跑")
	def jiayou(self):
		print("车在加油")
	def introduction(self):
		print("这款车是%s他的颜色是%s"%(self.name, self.color))


msld = car()
msld.name = "玛莎拉蒂"
msld.color = "黄色"
msld.move()
msld.jiayou()
msld.introduction()

lsls = car()
lsls.name = "劳斯莱斯"
lsls.color = "黑色"
lsls.move()
lsls.jiayou()
lsls.introduction()