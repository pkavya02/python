list = ['rama', 'sita', 1, 2]
print(list[0])
print(len(list))

list.append(3)
print(list)

list.remove('sita')
print(list)

list1 = [4,7,2,8,9,1 ]
list1.sort()
print(list1)

tuple = (1,2,3,'ram','ravi' )
print(tuple)
print(tuple[1])

def get_coordinates():
    return (3, 4)

x, y = get_coordinates()
print(x)
print(y)