# class decleration
'''
class sample():
    name = 'Eka'
    age = '21'
'''
# set, get & del attribute

'''
print(getattr(sample,'name'))
print(getattr(sample,'age'))
# print(getattr(sample,'gender')) It gives error
print(getattr(sample,'gender','No attribute')) # No such attribute


setattr(sample,'name','Raj')
setattr(sample,'gender','M')
print(sample.gender)
delattr(sample,'gender')
'''

# . Operator

'''
print(sample.name)
print(sample.age)
'''

# Methods in python

'''
class Student:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    def stud_details(self):
        print("Name : ",self.name," Gender : ",self.gender)

stud1 = Student('Eka','M')
stud1.stud_details()

stud2 = Student('Charlie','M')
stud2.stud_details()

print(stud1.__dict__) # simply prints the details in json format
print(stud2.__dict__) # simply prints the details in json format

'''


# Property Decorator

'''

class Student:
   def __init__(self,name,age):
       self.name = name
       self.age = age
       self.msg = 'The name is : '+self.name+' age is '+ str(self.age)
   def msg_func(self):
        return 'The name is : '+self.name+' age is '+ str(self.age)
obj = Student('Kapilan', 21)
print(obj.msg)
obj.age = 30  # Here age is changed
print(obj.msg) # But not print in msg variable

print(obj.msg_func()) # It will update and print in msg() function
obj.age = 45  # Here age is changed
print(obj.msg_func()) # It is print in msg() function

'''

# Property Decorator with Getter and Setter

'''
class Student:
   def __init__(self,name,age):
       self.name = name
       self._age = age # It is a private variable


   def setter(self,age):
       self._age = age
   def getter(self):
       return self._age
   age = property(getter, setter)


obj = Student('Kapilan', 21)
print(obj.name,' ',obj.age)
obj.age = 30  # Here age is changed
print(obj.name,' ',obj.age) # age is printed

'''


# Class Method Decorator

'''
class Student:
    count = 0 # Act like static in java
    def __init__(self,name,age):
       self.name = name
       self.age = age
       Student.count = Student.count + 1 # access the count variable with 'Student.count'
    def stud_details(self):
        print("Name : ",self.name," Age : ",self.age)
    @classmethod # Class Method Decorator for access count variable
    def tot(cls):
        return cls.count # Return the last updated value


obj1 = Student('Eka',21)
obj1.stud_details()
print("Total no of students ",obj1.tot())
obj2 = Student('Rajasekar',26)
obj2.stud_details()
print("Total no of students ",obj2.tot())
print("Total no of students ",obj1.tot())

'''

# Static Method in python

'''
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printDetail(self):
        print("Name : ",self.name," Age ",self.age)
    @staticmethod # Static method in python
    def welcome():
        print("Welcome to College")

s1 = Student('Vicky',21)
s1.printDetail()
s1.welcome()
s2 = Student('Jacky',20)
s2.printDetail()
s2.welcome()

'''