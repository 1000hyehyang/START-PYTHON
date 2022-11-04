answer = list(input())

n = len(answer)

total = 0
current = 1

for i in range(n):
	if answer[i]=='O':
		total = total + current
		current = current + 1
	elif answer[i]=='X':
		current = 1
	
print(total)
