group = ['A', 'B', 'C', 'D', 'E', 'F']
name = ['가영', '나은', '다희', '라율']

all_list = [group[0], name[:2], group[1:4], name[2], group[4:], name[-1]]
print(all_list)
['A', ['가영', '나은'], ['B', 'C', 'D'], '다희', ['E', 'F'], '라율']
