from functools import reduce

# 1. Find sum of all elements
# def sum(x,y):
#     return x+y
# l=[1,2,3,4,5]
# print(reduce(sum,l))

# 2. Find product of all elements
# def product(x,y):
#     return x*y
# l=[1,2,3,4]
# print(reduce(product,l))

# 3. Find maximum number
# def max(x,y):
#     return x if x>y else y
# l=[10, 25, 5, 40]
# print(reduce(max,l))

# 4. Find minimum number
# def min(x,y):
#     return x if x<y else y
# l=[10, 25, 5, 40]
# print(reduce(min,l))

# 5. Subtract all numbers
# def sub(x,y):
#     return x-y
# l=[20, 5, 3]
# print(reduce(sub,l))

# 6. Find sum of squares
# def sumofsq(x,y):
#     return x+x*y
# l=[1, 2, 3]
# print(reduce(sumofsq,l))

# 7. Count total elements
# def count(x,y):
#     return x+1
# l=[10, 20, 30, 40]
# print(reduce(count,l))

# 8. Find factorial of a number
# def fact(x,y):
#     return x*y
# l=5
# print(reduce(fact,range(1,l+1)))


# 9. Concatenate strings

# def concat(x,y):
#     return x+y
# l=["Hello", " ", "World"]
# print(reduce(concat,l))

# 10. Find largest string
# def check(x,y):
#     return x if len(x)>len(y) else y
# l=["hi", "python", "java"]
# print(reduce(check,l))

# 11. Sum of even numbers only
# def sumofeven(x,y):
#     if y%2==0:
#         return x+y
#     return x
# l=[1, 2, 3, 4, 5]
# print(reduce(sumofeven,l,0))

# 12. Count even numbers
def count(x,y):
    if y%2==0 :
        return x+1
    return x
l=[1, 2, 3, 4, 5]
print(reduce(count,l,0))