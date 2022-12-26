dict = {}
list_0 = []
total = 0
n = int(input())

for i in range(n):
    name = input()
    price = int(input())
    x = int(input())
    dict[name]= x
    list_0.append(price)

list_1 = list(dict.keys())
list_2 = list(dict.values())

for i in range(n):
    if list_2[i] < 3:
        list_2[i] = 3 - list_2[i]
    print('{0}:{1}개'.format(list_1[i],list_2[i]))

for i in range(n):
    total = total + list_0[i]*list_2[i]

print(total)
