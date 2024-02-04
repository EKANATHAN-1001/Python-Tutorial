a = int(input('Enter a number 1 '))
b = int(input('Enter a number 2 '))

# This is wrong 
print(a|b)


# This is correct only for +ve values.

while(b>0):
    c = a & b
    a = a ^ b
    b = c << 1

print(a)
