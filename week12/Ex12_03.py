def maxFunc(lst):
	max = 0
	for i in range(0,len(lst)):
		if max<lst[i]:
			max = lst[i]
		
	return max

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54] 
maxNum = maxFunc(A)
print(maxNum)
