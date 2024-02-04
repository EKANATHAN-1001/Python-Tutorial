try:
    a = 9/0 # Change 0 to any number to avoid exception.
    print(a)
except Exception as e:
    print("/ by Zero error")
else: # To access the variable 'a' present in 'try' block 
    print(a)
finally:
    print('done')