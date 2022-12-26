def judge(invest, data):
	base=invest
	for i in range(0,len(data)):
		invest = invest*(data[i]+100)/100
	
	pure = invest - base
	print(f'{int(pure)}')
	
	if pure>0:
		print('이득입니다.')
	elif pure<0:
		print('손해입니다.')
	else:
		print('본전입니다.')
	
lst = []
a = int(input('투자 액수를 입력하세요: '))
b = int(input('투자한 날짜 수를 입력하세요:'))

for i in range(b):
	temp = int(input(f'{i+1}일차 변동 데이터를 입력하세요: '))
	lst.append(temp)

judge(a, lst)
