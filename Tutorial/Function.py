# Arbitary arguments (more arguments)
'''
def stud_det(*student):
    print(student)
    for u in student:
        print(u)
stud_det('Eka','Raj','Vijay')
'''

# Adding n numbers
'''
def add(*value):
    sum = 0
    for i in value:
        sum = sum + i
    print(sum)

add(1,2,3)
add(2,3)
add(1)
'''

# Keyword arguments

'''
def func(a,b):
    print('a = ',a,' b = ',b)

func('b','a')
func(b='b',a='a')
'''

# Default arguments

'''
def func(name,city='MDU'):
    print('name = ',name,'city = ',city)

func('Eka','Chennai')
func('Ragu')
'''

# Lambda function

'''
c = lambda a,b : a+b

d = lambda a : a**2

# c(3,6) 
# print(c) This will only give address of lambda function

print(c(5,6))
print(d(4))
'''