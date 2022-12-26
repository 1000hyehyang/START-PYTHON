f = open('data/about_python.txt', 'r')
sentences = []
i=0

while True:
	data = f.readline()
	if data == '':
		break
	else:
		numbering = str(i+1)+'번 문장 '
		data = numbering + data
		sentences.append(data)
		i += 1
f.close()

f = open('data/about_python.txt', 'w')
for j in sentences:
	f.write(j)
f.close()

f = open('data/about_python.txt','r')
print(f.read())
f.close()
