time = input('请输入年月日')
def leap_year(year):
	if(year%100 != 0 and year%4 == 0) or year%400 == 0:
		return True
	else:
		return False
def year_month_day(year,month,day):
	day_sum = 0
	month31 = [1,3,5,7,8,10,12]
	month30 = [4,6,9,11]
	for i in range(1,month):	
		if i in month31:
			day_sum+=31
		elif i in month30:
			day_sum+=30
		elif leap_year(year):
			day_sum+=29
		elif i == 2:
			day_sum+=28
	day_sum+=day
	print('%s是今年的第%d天'%(time,day_sum))
def get_ymd(time):
	year = int(time[0:4])
	month = int(time[4:6])
	day = int(time[6:8])
	year_month_day(year, month, day)
get_ymd(time)
