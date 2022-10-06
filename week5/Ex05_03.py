start_day = 2  # Tuesday
last_day = 31

print('\tS\tM\tT\tW\tT\tF\tS')

for i in range (2):
	print('\t', end='')
	
for j in range(1,32):
	if j%7 !=5:
		print('\t%d' %j, end='')
		j += 1
	elif j%7 == 5:
		print('\t%d\n' %j)
		j += 1
