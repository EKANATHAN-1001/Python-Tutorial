# LIST

#  List Slicing

'''

a = [2,3,4,5]

print(a)
print(a[2])
print(a[-1::-1])
print(a[:3])
print(a[1:])


b = [3,'F','Hai',True,[1,2,3,4]]
print(b)
print(b[1])
print(b[-1])
print(b[2:])
print(b[-1][-1::-1])

b[2] = 'Bye'
b[-1][2] = 6
print(b)

'''

# List in-built function

'''
a = [1,2,3,4,5]
print(a)
a.clear()
print(a)


a = [1,2,3,4,5]
b = a # Change in any list affect other
print(b)
b[2] = 7
print(a,b)
a[2] = 8
print(a,b)

a = [1,2,3,4,5]
b = a.copy() # Change in any list doesn't affect other
print(b)
b[2] = 7
print(a,b)
a[2] = 8
print(a,b)



a = [1,2,3,4,3,2,7]

print(a.count(2))
print(a.index(2))
print(a.pop(3)) # Remove at position
print(a)
a.remove(3) # Remove by value one time
print(a)
'''

# List Aggregation

'''
a = [1,2,3,4,2,7]

print(len(a))
print(max(a))
print(min(a))

'''

# Append, Extend, Insert

'''
a = ['Hai']
print(a)
a.append('How') # Adding single value
a.append('are')
# a.append('you','?') It give error
print(a)

b = ['you','?','Fine']
a.extend(b) # Merge of 2 List
print(a,b)

b.insert(1,'No')
print(b)
'''

# list() function

'''
print(list(range(5)))
print(list('Hai Bro'))
'''

# List sort

'''

a = [3,56,76,1,435,8]
a.sort()
print(a)
a.sort(reverse = True)
print(a)

a = ['Apple','Orange','Yolk']
a.sort()
print(a)
a.sort(reverse = True)
print(a)
a.sort(key = len)
print(a)

'''



# TUPLE

# Tuple Slicing

'''
a = (1,'F',True,'How',(1,2,3))
print(a)
print(a[1])
print(a[-1])
print(a[1:])
print(a[-1][-1::-1])
'''

# Tuple can't be Change, but it is done by list()

'''
a = (1,'F',True,'How',(1,2,3))
b = list(a)
print(b)

b.insert(1,False)
print(b)

a = tuple(b)
print(a)
'''


# Speciality of tuple

'''
a = (1)
print(type(a)) # int
a = (1,)
print(type(a)) # tuple
'''

# Tuple concatenate

'''
a = (1,2,3,4)
b = (3,4,5,6)
c = a+b
print(c)

c = (a,b)
print(c)
'''