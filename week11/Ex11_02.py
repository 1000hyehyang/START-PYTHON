def average(k, e, m):
		return (k+e+m)/3
		
kor = int(input('국어 점수를 입력하세요: '))
eng = int(input('영어 점수를 입력하세요: '))
math = int(input('수학 점수를 입력하세요: '))

total_average = average(kor, eng, math)

print(f'국어는 {kor}점, 영어는 {eng}점, 수학은 {math}점이며, 총 평균은 {total_average:.2f}점입니다.')
