//<컴퓨팅 사고 소수 판단 프로그램>

"""숫자를 입력받아 input()

입력받은 횟수만큼 for문으로 반복하면서

소수(약수가 1과 자기자신만을 가지는 자연수) 판단 조건에 참일때 "소수입니다"를 출력하는 프로그램을 작성하시오"""

time = int(input())

n = 0

for i in range(1, time+1):
    if i!=1 and i!=time and time%i == 0:
        n = 1

if n == 0:
    print("소수입니다")
else:
    print("소수가 아닙니다")
