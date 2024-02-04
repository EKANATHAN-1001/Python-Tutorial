# Simple Inheritance

'''

class Nokia:
    company = 'Nokia India'
    website = 'www.nokia-india.com'

    def contact(self):
        print('Address : Vasuki st, Vandiyur nagar, Bengaluru')

class Nokia1100(Nokia): # Nokia1100 is Inherited from Nokia class
    def __init__(self):
        self.name = 'Nokia1100'
        self.year = 2020
    def product_Details(self):
        print('Name : ',self.name)
        print('Year : ',self.year)
        print('company : ',self.company)
        print('website : ',self.website)
        # self.contact()

m = Nokia1100()
m.contact()
m.product_Details()

'''

# Multiple Inheritance

'''

class Father:
    def chess(self):
        print('Chess from Father ')
    def work(self):
        print('Working...') 

class Mother:
    def chess(self):
        print('Chess from Mother ')
    def cook(self):
        print('Cooking...')
    
class son(Father,Mother):
#class son(Mother,Father):
    def ride(self):
        print('I am Riding ...')

s1 = son()
s1.ride()
s1.cook()
s1.work()
s1.chess() # Chess is available in both classes, It takes the first parent class method

'''

# Multilevel Inheritance

'''

class GrandFather:
    def own_House(self):
        print('Grand Father has House')
    def chess(self):
        print('Chess from GrandFather ')


class Father(GrandFather):
    def own_Bike(self):
        print('Father has Bike')
    def chess(self):
        print('Chess from Father ')

class Son(Father):
    def own_Book(self):
        print('Son has Book')

obj = Son()
obj.own_Book()
obj.own_Bike()
obj.own_House()
obj.chess() # Call immediate parent class method

'''

