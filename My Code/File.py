f = open('/home/admin/Documents/Python/My Code/f1.txt','r')
print(f.read())
str = 'Ohh File !'
f = open('/home/admin/Documents/Python/My Code/f1.txt','w')
f.write(str)
f = open('/home/admin/Documents/Python/My Code/f1.txt','r')
print(f.read())