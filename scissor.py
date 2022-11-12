
x = ['剪刀', '石頭', '布']
import random
y = random.choice(x)

#game = input('你想要比幾局呢?')
#game = int(game)

while True:
	play = input('您想要出剪刀、石頭還是布? ')
	if play == y:
		print(y)
		print('平手了，再一次!')

	elif play == '剪刀' and y == '布':
		print('你贏了!')
		print(y)

	elif play == '石頭' and y == '剪刀':
		print('你贏了!')
		print(y)

	elif play == '布' and y == '石頭':
		print('你贏了!')
		print(y)

	else:
		print('你輸了!')
		print(y)
		break


