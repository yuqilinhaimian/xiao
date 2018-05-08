class SweetPotato():


	def __init__(self):
		self.cookedLever = 0
		self.cookedStr = "生的"
		self.condliments = []

	def cook(self, time):
		self.cookedLever += time
		if self.cookedLever > 8:
			self.cookedStr = "烤糊了"
		elif self.cookedLever > 5:
			self.cookedStr = "烤熟了"
		elif self.cookedLever > 3:
			self.cookedStr = "半生不熟"
		else:
			self.cookedStr = "生的"

	def __str__(self):
		msg = self.cookedStr + "地瓜"
		if len(self.condliments) > 0:
			msg = msg + "("
			for temp in self.condliments:
				msg = msg + temp + ","
			msg = msg.strip(",")
			msg = msg + ")"
		return msg

	def addCondiments(self, condLiments):
		self.condliments.append(condLiments)

mySweetPotata = SweetPotato()
mySweetPotata.cook(5)
print(mySweetPotata.cookedLever)
print(mySweetPotata.cookedStr)

