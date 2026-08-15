# 2. Simple decorator
# def my_decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("after")
#     return wrapper
# @my_decorator
# def hello():
#     print("Helllo")
    
# hello()

# 3. Decorator without @
# def deco(func):
#     def wrapper():
#         print("decorated")
#         func()
#     return wrapper
# def show():
#     print("Show")
# show=deco(show)
# show()

# 4. Decorator with return value
# def deco(func):
#     def wrapper():
#         return func()+5
#     return wrapper
# @deco
# def num():
#     return 10

# print(num())