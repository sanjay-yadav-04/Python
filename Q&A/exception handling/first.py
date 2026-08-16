# q-1
# try:
#    with open("1.txt","r") as f:
#     print(f.read())
# except Exception as f:
#     print(f)
# try:
#    with open("2.txt","r") as f:
#     print(f.read())
# except Exception as f:
#     print(f)
# try:
#    with open("3.txt","r") as f:
#     print(f.read())
# except Exception as f:
#     print(f)

# q-2
# l=[1,2,3,4,5,6,7,8]
# for i,item in enumerate(l):
#     if i==2 or i==4 or i==6:
#         print(item)

# q-3
# n=int(input("Enter The Number:"))
# table=[n*i for i in range (1,11)]
# print(table)

# q-4
# try:
#   a=int(input("Enter The 1st Number:"))
#   b=int(input("Enter The 2nd Number:"))
#   print(a/b)
# except Exception as e:
#     print(e,"This Will create a infinite")

# q-5
n=int(input("Enter The Number:"))
table=[n*i for i in range(1,11)]
print(table)
with open("Tables.txt","a") as f:
    f.write(f" Table of {n} : {str(table)}\n")