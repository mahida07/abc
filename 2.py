# def calc_sum(a,b,c,d):
#     sum=a+b+c+d 
#     print(sum)
#     return sum

# calc_sum(3,6,3,8)

# def calc_prod(a,b):
#     return a*b


# def converter(USD_val):
#     PKR_val=USD_val*55
#     print(USD_val, "USD=" , PKR_val, "PKR") 
#     return converter
    
#     converter(1)


# def calc_factorial(n):
#     factorial=1
#     for i in range (1, n+1):
#         factorial*=i
#         print(factorial)
    
# calc_factorial(5)



# f = open("i.html", "a")
# data=f.read()
# data=f.read(9)
# print(data)
# print(type(data))
# f.close()


# write= f.write("yayyyyyyyyyyyyyyyy")

# write=f.write("hiiiiiiiii")


# f=open("i.html","+a")
# print(f.read())
# f.close()


# word="hiii"
# with open("abc.html","r") as f:
#     data= f.read()
#     if(data.find(word)!=-1):
#         print("found")
#     else:
#         print("not found")




# import os
# os.remove("123.txt")



import random

uppercase_letters="ABCDEFG"
lowercase_letters=uppercase_letters.lower()
digits="1234567890"
symbols="!@#$%^&*()_+><?:|"

upper,lower,digs,syms=True,True,True,True

all=""

if upper:
    all+= uppercase_letters
if lower:
    all+= lowercase_letters
if digs:
    all+= digits
if syms:
    all+= symbols


lenght=12
amount=15
 

for x in range(amount):
    password="".join(random.sample(all,lenght))
    print(password)

