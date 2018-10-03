AFC_east = ['New England Patriots', 'Bafflo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42,123]
empty = []
print (AFC_east, numbers, empty)
print ('Bafflo Bills' in AFC_east)
# ['spam',2.0, 5, [10,20]]
AFC_east[3] = 'New York Giants'
print (AFC_east)

#Traversing a list
for team in AFC_east:
    print(team)
numbers = [2,0,1,6,9]
for i in range(len(numbers)):
    numbers[i]=numbers[i]*2

print(numbers)

my_list = ['spam', 1, ['New England Patriots',\
                         'Buffalo Bills', 'Miami Dolphins',\
                         'New York Giants'],\
                         [1, 2, 3]]
print(len(my_list))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

[0] *4
t = ['a', 'b', 'c', 'd', 'e', 'f']
# t[1:3] = ['x','y']
# print(t)
# print(t[1:3])
# print(t[3:6])
t.append('z') #Add an item to the end of the list
print(t)
t.extend('e')
print(t)
t.sort(key=None, reverse=False)
print(t)