# Python id & types
''' 

a = 90
print(a)
print(chr(a))
print(id(a))
print(type(a))
print(type(chr(a)))
print(id(a))

'''

# Python keywords

'''
import keyword
print(keyword.kwlist)
'''


# Standard I/O

'''
a = input('Enter a number 1 ')
b = input('Enter a number 2 ')
print(a+b)


a = int(input('Enter a number 1 '))
b = int(input('Enter a number 2 '))
print(a+b)


a = float(input('Enter a number 1 '))
b = float(input('Enter a number 2 '))
print(a+b)

a = chr(input('Enter a number 1 ')) # input() is function takes string as input. It can't directly convert to char dtype. 
b = chr(input('Enter a number 2 '))
print(a+b)

a,b,c = input("Enter any values seperate by space ").split()
print(a,b,c)

text = """ Hai I am working on python 
this is new program that I learnt."""
print(text)
'''

# Strings

s = 'Hai pandi how are you'
'''
print(s)
print(s.isupper()) # False
print(s.islower()) # False


s = s.upper() # HAI PANDI HOW ARE YOU
print(s) 
print(s.isupper()) # True


s = s.lower() # hai pandi how are you
print(s)
print(s.islower()) # True


print(s.capitalize())
print(s.title())

print(s.count('a'))
print(s.endswith('you'))
print(s.startswith('Hai'))

print(s.find('z')) # No character is found so '-1' output
print(s.find('a')) # Position of the first char 'a' is 1

print(s.replace('a','i'))
print(s.replace('ai','ea'))
print(s.replace('z','a'))


print(s.isalnum())

s = 'Hai pandi how are you 123'
print(s.isalnum())
s = 'Haipandihowareyou123'
print(s.isalnum())
s = 'Haipandihowareyou123'
print(s.isalpha())
s = 'Haipandihowareyou'
print(s.isalpha())

s = '    Hai    '
print(len(s)) # len = 11
print(len(s.strip())) # len = 3
print(len(s.rstrip())) # len = 7
print(len(s.lstrip())) # len = 7



s = "HelloWorld!"
print(s) 
print(s[:3])
print(s[1:6])
print(s[6:])
print(s[-1])
print(s[-1::-1])

'''