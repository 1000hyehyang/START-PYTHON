finder = True
company = []
index = -1

while finder:
	what = input('어떤 작업을 진행하시겠습니까? 끝내길 원하신다면 \'종료\'를 입력하세요: ')
	
	if what == '종료':
		print('종료합니다')
		finder = False
	elif what == '입력':
		name = input('자회사 이름: ')
		data1 = input('유동자산: ')
		data2 = input('재고자산: ')
		data3 = input('유동부채: ')
		
		company.append([name, data1, data2, data3])
		index += 1
		print(company)

	elif what == '추출':
		if index<0:
			print('정보가 없습니다')
		else:
			print(f'{company[0][0]} 자회사의 유동자산은 {company[0][1]}만원, 재고자산은 {company[0][2]}만원, 유동부채는 {company[0][3]}만원입니다.')
			company.remove(company[0])
			index -= 1
	else:
		print('잘못된 입력입니다')
