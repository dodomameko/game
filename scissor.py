
x = ['剪刀', '石頭', '布']
import random
y = random.choice(x)
w = 0 #贏局
l = 0 #輸局
d = 0 #和局

while True:
	g = input('你想要比幾局呢? ')
	g = int(g)
	if g < 3:
		print('至少要比三局唷!')
	else:
		break

while True:
	play = input('您想要出剪刀、石頭還是布? ')
	print('電腦出'+y)
	g = g-1

	if play == y:
		d = d+1
		print('平手了!')
		print('剩下',g,'局',w ,'勝',l ,'敗',d ,'平手')

	elif play == '剪刀' and y == '布':
		w = w+1
		print('你贏了!')
		print('剩下',g,'局',w ,'勝',l ,'敗',d ,'平手')

	elif play == '石頭' and y == '剪刀':
		w = w+1			
		print('你贏了!')
		print('剩下',g,'局',w ,'勝',l ,'敗',d ,'平手')

	elif play == '布' and y == '石頭':
		l = l+1			
		print('你贏了!')
		print('剩下',g,'局',w ,'勝',l ,'敗',d ,'平手')

	else:
		l = l+1			
		print('你輸了!')
		print('剩下',g,'局',w ,'勝',l ,'敗',d ,'平手')

	if g == 0:
		print('最後結果是',w ,'勝',l ,'敗',d ,'平手')
		print('遊戲結束!')
		if w > l:
			print('你贏電腦了!')
		elif w < l:
			print('你輸電腦了!')
		else:
			print('沒輸沒贏!')
		break



