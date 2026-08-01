# 1. Filter even numbers
# def fil(x):
#     if(x%2==0):
#         return x
# l=[1,2,3,4,5]
# print(list(filter(fil,l)))

# 2. Filter odd numbers
# def odd(x):
#     return x%2!=0
# l=[1,2,3,4,5]
# print(list(filter(odd,l)))

# 3. Filter positive numbers
# def positive(x):
#     return x>0
# l=[-2, -1, 0, 3, 5]
# print(list(filter(positive,l)))

# 4. Filter negative numbers
# def negative(x):
#     return x<0
# l=[-2, -1, 0, 3, 5]
# print(list(filter(negative,l)))

# 5. Filter non-zero numbers
# def check(x):
#     return x!=0
# l=[-2, -1, 0, 3, 5]
# print(list(filter(check,l)))

# 6. Numbers greater than 10
# def check(x):
#     return x>10
# l=[5, 12, 8, 20]
# print(list(filter(check,l)))

# 7. Numbers divisible by 3
# def check(x):
#     return x%3==0
# l=[3, 5, 6, 9, 10]
# print(list(filter(check,l)))

# 8. Numbers divisible by 2 and 5
# def check(x):
#     if(x%2==0 and x%5==0):
#         return x
# l=[10, 20, 25, 40]
# print(list(filter(check,l)))

# 9. Numbers less than 50
# def check(x):
#     return x<50
# l=[20, 55, 40, 70]
# print(list(filter(check,l)))

# 10. Filter zero only
# def check(x):
#     return x==0
# l=[0, 1, 0, 2]
# print(list(filter(check,l)))

# 16. Strings length > 5
# def check(x):
#     return len(x)>5
# l=["python", "java", "programming"]
# print(list(filter(check,l)))

# 17. Strings starting with vowel
# def check(x):
#     return x[0].lower() in "aeiou"
# words=["apple","bananna","orange"]
# print(list(filter(check,words)))

# 18. Strings ending with 'n'
# def check(x):
#     return x.endswith('n')
# l=["apple","bananan","orange"]
# print(list(filter(check,l)))

# 19. Uppercase strings
# def check(x):
#     return x.isupper()
# l=["PYTHON", "Java", "HTML"]
# print(list(filter(check,l)))

# 20. Lowercase strings
# def check(x):
#     return x.islower()
# l=["PYTHON", "java", "HTML"]
# print(list(filter(check,l)))

# 21. Strings containing 'a'
# def check(x):
#     return 'a' in x
# l=["PYTHON", "Java", "HTML"]
# print(list(filter(check,l)))