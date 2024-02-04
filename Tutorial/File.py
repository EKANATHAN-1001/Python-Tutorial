# Read with read() method 
'''
f = open('F1.txt')
print(f.read(),'\n') # Read entire Text File
'''

# Read with readline() method 
'''
f1 = open('F1.txt')
print(f1.readline()) # Read first line of the text file
print(f1.readline(4)) # Read the specified no. of character from the current cursor position
'''

# Read with readlines() method
'''
f2 = open('F1.txt')
print(f2.readlines()) # Read all the lines in file and outputs in string array

f2 = open('F1.txt')
msg = f2.readlines()
print(msg[1])# prints the second line of the file
'''

# Loop line by line in File
'''
f3 = open('F1.txt')
for l in f3:
    print(l)
'''


# write into a file
'''
f = open('F1.txt','w')
msg = 'Good Morning'
f.write(msg)
'''

# append into existing file
'''
f = open('F1.txt','a')
msg = '\nFine ?'
f.write(msg)
'''

# Delete a file 
'''
import os 

os.remove('F1.txt') # File is removed from disk 

if os.path.exists('/media/admin/B.Tech_IT/IT-BIT-R19.pdf'):
    print('File is available in the path')
else:
    print('File is not available in the path')
'''

# Create and Delete a directory

# Create directory
'''
import os
os.mkdir('NewFolder :)')
'''
# Delete directory
'''
import os
os.rmdir('NewFolder :)')
'''