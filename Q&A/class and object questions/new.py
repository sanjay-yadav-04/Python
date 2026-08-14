# #Q-Create a class Mobile that stores brand, model, price and apply discount.
# class Mobile:
#     def __init__(self,brand,model,price):
#           self.brand=brand
#           self.model=model
#           self.price=price
#     def discount(self,percent):
#          discount=self.price * percent/100
#          final_price=self.price-discount
#          return final_price
# n1=Mobile("Samsung","s21",80000)
# print(n1.discount(10))

#BankAccount Class Deposit, withdraw and check balance
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def withdraw(self,amount):
#         if amount<=self.balance:
#              self.balance-=amount
#         else:
#             print("Insufficient funds")
#     def deposit(self,amount):
#         self.balance+=amount
#     def checkalance(self):
#         print(self.balance)
# acc1=BankAccount("sanjay",1000)
# acc1.deposit(500)
# acc1.withdraw(300)
# acc1.checkalance()

# 3. Class with attribute
# class Person:
#     name="sanjay"
# obj=Person()
# print(obj.name)

# 4. Change object attribute
# class Person:
#     name="sanjay"
# obj=Person()
# obj.name="Yadav"
# print(obj.name)

# 5. Multiple objects
# class Person:
#     name="Sanjay"
#     surname="yadav"
# obj1=Person()
# obj2=Person()\
    
# print(obj1.name)
# print(obj2.name)

# 6. Method inside class
# class Person:
#    def gree(self):
#        print("Hello")
# obj=Person()
# obj.gree()

# 8. Instance variable
# class Person:
#     def intro(self,name):
#         self.name=name
# obj=Person()
# obj.intro("sanjay")
# print(obj.name)

# 9. Access instance variable
# class Car:
#     def __init__(self):
#         self.brand="TAta"
# obj=Car()
# print(obj.brand)


# 10. Constructor (__init__)
# class Emp:
#     def __init__(self,name):
#         self.name=name
# p1=Emp("sanjay")
# print(p1.name)

# 12. Multiple attributes
# class Student:
     
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Student("Aman",31)
# s2=Student("Sanjay",20)
# print(s1.name,s2.name)        
    
# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def show(self):
#         print(self.marks)
# s1=Student("sanjay",20,90)
# s1.show()

# 14. Default constructor value
# class Demo:
#     def __init__(self,x=10):
#         self.x=x
# ans=Demo()
# print(ans.x)

# 15. Class variable
# class New:
#     name="sanjay"
# print(New.name)

# 16. Access class variable via object
# class New:
#     name="sanjay"
# obj=New()
# print(New.name)

# 17. Modify class variable
# class New:
#     name="sanjay"
# obj=New()
# obj.name="Vipin"
# print(obj.name)

# 18. Instance vs Class variable\\
    
# class New:
#     x=10
# n=New()
# n.x=20
# print(n.x,New.x)

# 19. Delete object property
# class New:
#     def __init__(self):
#         self.x=5
# obj=New()
# del obj.x
# print(hasattr(New, 'x'))


# 21. Two methods in class
# class Marks:
#     def add(self):
#         print(2+5)
#     def sub(self):
#         print(3-5)
# obj=Marks()
# obj.add()
# obj.sub()

# 22. Return value from method
# class Maths:
#     def add(self,x,y):
#         self.x=x
#         self.y=y
#         return x+y
# obj=Maths()
# print(obj.add(3,2))
        
# 23. Object as argument
# class New:
#     def show(self):
#         print("Hello")
# def display(obj):
#     obj.show()
# t=New()
# display(t)

# 24. Static method
# class New:
#     @staticmethod
#     def show():
#         print("Hello")
# obj=New()
# obj.show()

# 25. Class method
# class New:
#     x=10
#     @classmethod
#     def show(cls):
#         print(cls.x)
# obj=New()
# obj.show()
    
# # 26. Count objects
# class Count:
#     c=0
#     def __init__(self):
#         Count.c+=1
# a=Count()
# b=Count
# print(Count.c)

# 27. __str__ method
# class A:
#     def __str__(self):
#         return"Hello"
# obj=A()
# print(obj)


# 28. __del__ method
# class New:
#     def __del__(self):
#         print("Object deleted")
# a=New()
# del a


# Real world examples questions
# Create a class to store student name and marks and display result.

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def result(self):
#         print(f"Name Of student is {self.name} And Marks Are {self.marks}")
        
# s1=Student("Sanjay",20)
# s1.result()
# s2=Student("Aman",50)
# s2.result()

# Create a bank account with deposit and withdraw.
# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposite(self,amount):
#         self.balance+=amount
#         print("Balnce=",self.balance)
#     def withdrawl(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Balance:", self.balance)
#         else:
#             print("Insufficient balance")
# b=Bank(1000)
# b.deposite(500)
# b.withdrawl(2000)
        
# Calculate total salary including bonus.
# class Employee:
#     def __init__(self,name,salary,bonus):
#         self.name=name
#         self.salary=salary
#         self.bonus=bonus
#     def total_Sal(self):
#         print(self.salary+self.bonus)
# e1=Employee("sanjay",10000,2000)
# e1.total_Sal()

# Add items and calculate total price.
# class Cart:
#     def __init__(self):
#         self.total=0
#     def add_item(self,price):
#         self.total+=price
#     def show_total(self):
#         print(self.total)
# c=Cart()
# c.add_item(1000)
# c.show_total()


# Simulate ATM withdrawal.
# class Atm:
#     def __init__(self,pin,balance):
#         self.pin=pin
#         self.balance=balance
#     def withdrawl(self,enter_pin,amount):
#         if enter_pin==self.pin:
#             if amount<=self.balance:
#                 self.balance-amount
#                 print("Current Balance=",self.balance)
#                 print("Withrawl=",amount)
#                 total_bal=self.balance-amount
#                 print("Total Balance =",total_bal)
#             else:
#                 print("Not Enough Balance")
#         else:
#             print("Entered wrong pin")
# atm=Atm(1234,5000)
# atm.withdrawl(1234,1000)


# Issue and return books.
# class Library:
#     def __init__(self):
#         self.book=5
#     def issue(self):
#         if self.book>0:
#             self.book=-1
#             print("Book Issued")
#         else:
#             print("No Book Issued")
#     def return_book(self):
#         self.book+=1
#         print("Book returned")
# l=Library()
# l.issue()
# l.return_book()

# Calculate order bill with delivery charge.
# class order:
#     def __init__(self,amount):
#         self.amount=amount
#     def bill(self,dilivery_charge):
#         self.delivery_charge=dilivery_charge
#         total_charge=self.amount+self.delivery_charge
#         print("Totalamount=",total_charge)
# o=order(1000)
# o.bill(500)
        
# Check fuel after driving.
# class Car:
#     def __init__(self,fuel):
#         self.fuel=fuel
#     def check(self,km):
#         self.fuel=self.fuel-km*0.5
#         print("Fuel left",self.fuel)
# me=Car(20)
# me.check(10)
        
# Recharge mobile balance.
# class Mobile:
#     def __init__(self,balance):
#         self.balance=balance
#     def recharge(self,amount):
#         self.balance+=amount
#         print("Balnce",self.balance)
# m=Mobile(50)
# m.recharge(199)

# Mark student present or absent.
# class Attendance:
#     def __init__(self,name):
#         self.name=name
#     def mark(self,present):
#         if present:
#             print(self.name,"Is Present")
#         else:
#            print(self.name,"Is Absent")
# s1=Attendance("Sanjay")
# s1.mark(True)

# 🔹 11. Hospital Patient System
# class Patient:
#     def __init__(self,name,days):
#         self.name=name
#         self.days=days
        
#     def bill(self,amount):
#         print("Total Bill Is:",self.days*amount)
# p=Patient("sanjay",3)
# p.bill(1500)

# 🔹 12. Electricity Bill
# class Electricity:
#     def __init__(self,units):
#         self.units=units
#     def bill(self,amount):
#         print("Total Bill Is :",self.units*amount)
# house1=Electricity(120)
# house1.bill(6)

# 🔹 13. Movie Ticket Booking
# class Ticket:
#     def __init__(self,seat):
#         self.seat=seat
#     def price(self,amount):
#         print("Total price Is:",self.seat*amount)
# p1=Ticket(3)
# p1.price(180)

# 🔹 14. Login System
# class Login:
#     def __init__(self,password):
#         self.password=password
#     def check(self,enterd_password):
#         if enterd_password==self.password:
#             print("Login Sucessfull")
#         else:
#             print("Incorrect password")
# p1=Login(123)
# p1.check(123)

# 🔹 15. Bus Ticket System
# class Bus:
#     def __init__(self,tickets):
#         self.tickets=tickets
#     def book(self,n):
#         if n<=self.tickets:
#             self.tickets-=n
#             print("Booked")
#         else:
#             print("Not Enough")
# b=Bus(10)
# b.book(4)
        
        
# 🔹 16. Online Exam Result
# class Exam:
#     def __init__(self,name,roll_no,marks):
#         self.name=name
#         self.roll_no=roll_no
#         self.marks=marks
#     def result(self,roll_no):
#         if roll_no==self.roll_no:
#             if self.marks>=40:
#              print(f"{self.name} has scored {self.marks} And Passed the examination")
#             else:
#                print(f"{self.name} has scored {self.marks} And Failed in the examination")
#         else:
#             print("Incorrect Roll Number")
# studen1=Exam("Sanjay",123,45)
# studen1.result(125)

# 🔹 17. Parking System
# class Parking:
#     def __init__(self,slots):
#         self.slots=slots
#     def bill(self):
#         amount=50
#         print("Total Bill Is",self.slots*amount)
# car1=Parking(4)
# car1.bill()

# Instance variable
# class Bank:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def show(self):
#         print(self.name,self.balance)
# p1=Bank("sanjay",12000)
# p1.show()

# 🔷 2. Class Variables (Real-World)
# class Student:
#     school="DPS school"
#     def __init__(self,name,roll_no):
#         self.name=name
#         self.roll_no=roll_no
#     def show(self):
#         print(self.name,self.roll_no)
# s1=Student("sanjay",21)
# s2=Student("Nitin",50)
# s1.show()
# s2.show()
# print(s1.school)
# s2.school="NRI"
# print(s2.school)

# 🔹 Type 3: Class Variable Used as Counter
class Employee:
    count=0
    def __init__(self):
        Employee.count+=1
p1=Employee()
p2=Employee()
print(Employee.count)