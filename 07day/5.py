high = int(input('请输入身高：')).0
shenjia = int(input('请输入身价：'))
facein = int(input('请输入颜值：'))
-

if high > 180 and shenjia > 1000000 and facein >99:
	print('高富帅')
elif high <= 180 and shenjia > 1000000 and facein >99:
	print('富帅')
elif high <= 180 and shenjia <= 1000000 and facein >99:
	print('帅')
elif high < 160 and shenjia < 1000 and facein <60:
	print('low逼')
else:
	print('输入错误')