# Date & Time

'''
import datetime as dt

today = dt.date.today() #  For current Date
print(today)

time = dt.datetime.now() # For current Time
print(time)
'''

# Date
 
'''
print(today.year)
print(today.month)
print(today.day)
'''

# Time

'''
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)
'''

# User defined date and time

'''
Date = dt.date(2020,5,2)
print(Date)

Time = dt.time(12,20,3)
print(Time)


Date1 = dt.date.today()
print(Date1-Date)
'''

# Date and time format

'''
print(today.strftime("%A %B %D")) # Various formats are available refer in online
'''