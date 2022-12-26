import math

def LCM(data1, data2):
	gcd = math.gcd(data1, data2)
	result = (data1*data2)//gcd
	return result

a = int(input('첫 번째 자연수를 입력합니다: '))
b = int(input('두 번째 자연수를 입력합니다: '))

print(float(LCM(a, b)))
