f = open('data/meerkat.txt','r')

while True:
	data = f.read()
	if data == '':
		break
	elif '서식지' in data:
		print(data)
	
f.close()
