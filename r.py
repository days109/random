a = input('請輸入起始值: ')
b = input('請輸入最大值: ')
a = int(a)
b = int(b)
import random
r = random.randint(a, b)
count = 0
while True:
	count += 1
	num = input('請輸入數字: ')
	num = int(num)
	if r == num:
		print('猜對了')
		break
	elif num > r:
		print('比較大喔')
	else:
		print('比較小喔')
	print('這是你猜的第', count, '次')
