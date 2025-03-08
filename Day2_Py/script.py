# mylist = [1,2,3,4,5,6,60,9]
# mylist2 = ["apple","kiwi","banana"]
# # sum=0
# # for i in mylist:
# #     sum=sum+i
# # print(sum)
# mylist.sort()
# print(mylist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist.insert(2,"blackcurrant")
# thislist.append("bruh") #pot adauga element ca string total
# thislist.extend("bruh") # imi pune in lista firecare litera a cuvantului
# print(thislist)

# from numpy import unique


# mylist =[]
# frecventa=[]
# newlist=[]
# counter = 1
# print("introdu n")
# n=int(input())
# for i in range(n):
#     print(f"introdu element in lista")
#     mylist.append(input())
# print(mylist)
# print("==========after=======")
# for i in range(len(mylist)):
#     for j in range(i+1,len(mylist)):
#         if(mylist[i]==mylist[j]):
#             counter=counter+1
#     if(counter!=0):
#         newlist.append([counter,mylist[i]])
#         mylist[i]=newlist[]
#     counter = 0
    

# Write a program that converts Fahrenheit to Celsius
# print("introdu grade fahrenheit")
# grade_introduse = int(input())
# grade_celsius = (grade_introduse-32)*5/9
# print(f"sunt atatea grade celsius {grade_celsius:.2f}")

# Check if a number is prime or not.
# a = int(input())
# flag = 1
# for i in range(2,a):
#     if(a%i==0):
#         flag = 0
#         break
# if(flag==1):
#     print("a este prim")
# else:
#     print("a nu e prim")

#Find the sum of all numbers from 1 to N.
# sum = 0 
# print("introdu n: ")
# n=int(input())
# for i in range(n+1):
#     sum=sum+i
# print(f"suma lor este: {sum}");

# Print multiplication table of a given number.
# print("introdu nr: ")
# n=int(input())
# for i in range(10):
#     print(i*n)

# print("cate iteratii vrei sa aiba fibonacci ")
# n=int(input())
# fibo = [0 for i in range(n)]
# for i in range(n):
#     if(i==0 or i==1):
#         fibo[i]=1
#     else:
#         fibo[i]=fibo[i-1]+fibo[i-2]
# print(fibo)

# import numpy as np

# sir_primit =input()
# sir_dorit = []
# for i in range(len(sir_primit)):
#     sir_dorit.append([i,sir_primit[i]])
# sir_dorit = np.unique(sir_dorit)
# print(sir_dorit)