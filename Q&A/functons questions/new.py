# # # # # # # # # # # # # # # 1. Write a function to print “Hello World”.
# # # # # # # # # # # # # # # def greet():
# # # # # # # # # # # # # # #     print(("Hello"))
# # # # # # # # # # # # # # # greet()
# # # # # # # # # # # # # # # 2. Write a function that takes a name and prints it.
# # # # # # # # # # # # # # def name(n):
# # # # # # # # # # # # # #     print(n)
# # # # # # # # # # # # # # n=input("Enter Your Name:")
# # # # # # # # # # # # # # name(n)
# # # # # # # # # # # # # # 3. Write a function to add two numbers.
# # # # # # # # # # # # # def add(a,b):
# # # # # # # # # # # # #     print(a+b)
# # # # # # # # # # # # # add(3,2)
# # # # # # # # # # # # # 4. Write a function to find the square of a number.
# # # # # # # # # # # # def square(n):
# # # # # # # # # # # #     print(n*n)
# # # # # # # # # # # # n=int(input("Enter the number:"))
# # # # # # # # # # # # square(n)
# # # # # # # # # # # # Write a function that returns the cube of a number.
# # # # # # # # # # # def cube(n):
# # # # # # # # # # #     return n*n*n
# # # # # # # # # # # n=int(input("enter the number:"))
# # # # # # # # # # # res=cube(n)
# # # # # # # # # # # print(res)
# # # # # # # # # # # 6. Write a function to print numbers from 1 to 10.
# # # # # # # # # # def num(n):
# # # # # # # # # #     for i in range(1,11):
# # # # # # # # # #         print(i)
# # # # # # # # # # num(10)
# # # # # # # # # # Write a function to check if a number is even.
# # # # # # # # # def even(n):
# # # # # # # # #     if n%2==0:
# # # # # # # # #         print("Even Number")
# # # # # # # # #     else:
# # # # # # # # #         print("Odd Number")
# # # # # # # # # n=int(input("Enter The Number:"))
# # # # # # # # # even(n)
# # # # # # # # # 8. Write a function to check if a number is odd.
# # # # # # # # def odd(n):
# # # # # # # #     if n%2!=0:
# # # # # # # #         print("Odd Number")
# # # # # # # #     else:
# # # # # # # #         print("Even Number")
# # # # # # # # n=int(input("enter The Number:"))
# # # # # # # # odd(n)
# # # # # # # # Write a function to find the factorial of a number.
# # # # # # # def factorial(n):
# # # # # # #     fact=1
# # # # # # #     for i in range(1,n+1):
# # # # # # #         fact *= i
# # # # # # #     return fact
# # # # # # # n=int(input("Enter The Number:"))
# # # # # # # res=factorial(n)
# # # # # # # print(res)
# # # # # # # Write a function to print a message multiple times
# # # # # # def mess(n):
# # # # # #   for i in range(1,11):
# # # # # #     print("hello ")
# # # # # # mess(10)
# # # # # # # 11. Write a function to return the largest of two numbers.
# # # # # def largest(x,y):
# # # # #     if x>y:
# # # # #         return "1st is laregst",x
# # # # #     else:
# # # # #         return '2n is largest',y
# # # # # x,y=int(input("Enter 1st The Number:")),int(input("Enter The 2nd Number:"))
# # # # # print(largest(x,y))
# # # # # 12. Write a function to return the smallest of two numbers.
# # # # def smallest(x,y):
# # # #     if x<y:
# # # #         return "1st is smallest",x
# # # #     else:
# # # #         return "2nd is smallest",y
# # # # x,y=int(input("Enter 1st Number:")),int(input("Enter 2nd Number:"))
# # # # print(smallest(x,y))
# # # # 13. Write a function to check if a number is positive.
# # # def check(n):
# # #     if n>=0:
# # #         print("Yes it is positive number")
# # #     else:
# # #         print("Its A Negative Number")
# # # n=int(input("Enter The Number:"))
# # # check(n)
# # # 14. Write a function to check if a number is negative.
# # def check(n):
# #     if n<=0:
# #         print("yes Its A Negative Number")
# #     else:
# #         print("Its A positive Number")
# # n=int(input("Enter The Number:"))
# # check(n)
# # 15. Write a function to calculate simple interest.
# def interest(p,r,t):
#     return p*r*t/100
# p=int(input("Enter The Principle Amount:"))
# r=int(input("Enter The Principle rate:"))
# t=int(input("Enter the time:"))
# res=interest(p,r,t)
# print(res)
# 16. Write a function to calculate area of a circle.
def area(n):
    return 3.14*n*n
n=int(input("Enter The Radius Of circle:"))