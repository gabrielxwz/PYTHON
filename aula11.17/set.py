'''
# Set - conjuntos

set01 = set('Paulo')
print(set01)

set02 = {'Paulo', 'Junior', 'Lara', 'Junior', 'Kaynan', 'Junior', 'Felipe', 'Junior'}
print = (set02)
'''
list = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5,]
print (list)
set03 = set(list)
print(set03)
print(5 in set03)
print(7 in set03)
print(7 not in set03)
print(5 not in set03)

for i in set03:
    print(i)

set03.add('Paulo')
set03.add(6)