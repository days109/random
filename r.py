import random
r = random.randint(1,100)
while True:
	num = input('請輸入數字: ')
	num = int(num)
	if r == num:
		print('於猜對了')
		break
	elif num > r:
		print('比較大喔')
	else:
		print('比較小喔')
