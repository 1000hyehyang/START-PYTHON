A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = sorted(A)
F = open('data/out.txt', 'w')

for i in A:
    data = str(i)
    F.write('%s' %data)
	
F.close()
