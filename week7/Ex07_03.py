num_list = []
sum=0

while True:
  
  num = int(input('몇 개를 입력하시겠습니까?'))
	if num < 0:
		print('다시 입력하세요')
	else:
		break
	
for i in range (1, num+1):
	data = int(input('넣을 숫자를 입력하세요:'))
	num_list.append(data)
	sum = sum+ num_list[-1]
	
print(num_list)
print('총합: %d' %sum)
