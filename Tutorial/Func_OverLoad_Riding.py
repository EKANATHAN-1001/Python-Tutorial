# Method OverRiding 

''' 

class Employee:
    def HrsToWork(self):
        self.hrs = 8
    def printDetails(self):
        print('Hrs to Work : ',self.hrs)

class Intern(Employee): # Intern is Inherited from Employee
    def HrsToWork(self):
        self.hrs = 6
    def reset_Hrs(self):
        super().HrsToWork()

E = Employee()
E.HrsToWork() # Calls the Employee function
E.printDetails()

I = Intern()
I.HrsToWork() # Calls the Intern function
I.printDetails()

I.reset_Hrs() # Calls the Employee function
I.printDetails()

'''

# Operator OverLoading

'''

class Operator_OverLoad:
    def __init__(self,a):
        self.a = a
    def __add__(o1,o2):
        return o1.a+o2.a 
    def __sub__(o1,o2):
        return o1.a-o2.a 
    def __mul__(o1,o2):
        return o1.a*o2.a 
    def __truediv__(o1,o2):
        return o1.a/o2.a

o1 = Operator_OverLoad(40)
o2 = Operator_OverLoad(30)

print('Total ',(o1+o2))
print('Total ',(o1-o2))
print('Total ',(o1*o2))
print('Total ',(o1/o2))

'''

# Abstract Base Class 'ABC'

'''

from abc import ABC, abstractmethod

class Library(ABC):
    @abstractmethod
    def borrow(self):
        pass
    @abstractmethod
    def Breturn(self):
        pass
    @abstractmethod
    def check(self):
        pass
class Dept_Lib(Library):
    def borrow(self):
        print('Borrow from Dept. Library')
    def Breturn(self):
        print('Return to Dept. Library')
    def check(self):
        print('Check book in Dept. Library')

obj = Dept_Lib()
obj.borrow()
obj.Breturn()
obj.check()

'''