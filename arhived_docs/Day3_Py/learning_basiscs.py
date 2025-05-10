
import numpy as np

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)

# print(quicksort([3,6,8,10,1,2,1]))


# x = 3
# print(x, type(x))

# print(~x)   


#Practice exercises 1:
# print("baga un string: ")
# s=input()
# print("baga un nr: ")
# n=int(input())
# r=True

# if(r==True):
#     result = n * s.replace(s[0],s[len(s)-1])
# else:
#     result = n*f"{s}"
# print(result)


# xs = [3,1,2]


# for i in range(len(xs)):
#     print(f"{xs[i]} | ")

# xs.append(4)

# for i in range(len(xs)):
#     print(xs[i])

# xs.pop(2)


# for i in range(len(xs)):
#     print(xs[i])


#Practice 2:
# arr = ["one", 2, 3, True, 5, "Six", "SeVen", 8, False, 10]
# nnumbers = 0
# nstrings = 0
# nbools = 0

# for i in range(len(arr)):
#     if(type(arr[i])==int):
#         nnumbers+=1
#     elif(type(arr[i])==str):
#         nstrings+=1
#     elif(type(arr[i])==bool):
#         nbools+=1
  
# print('We have {} numbers, {} strings, and {} booleans.'.format(nnumbers, nstrings, nbools))

# d = {'person': 2, 'cat': 4, 'spider': 8}
# for key, value in d.items():
#     print('A {} has {} legs'.format(key, value))

#Practice 3:
# letters = {}
# string = "This is the test string"

# for i in range(len(string)):
#     if(string[i]!=" "):
#         letters[string[i]]=string.count(string[i])

# print(letters)

#Practice 4:
# arr1 = [1, 2, 3, 5, 7, 8, 9]
# arr2 = [2, 4, 5, 6, 8, 10]

# arr1 = list(set(arr1))
# arr2 = list(set(arr2))


# counter = 0
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         if(arr1[i]==arr2[j]):
#             counter+=1
# print(counter)


#Practice 5
# def fibo(n):
#     if(n<=1):
#         return n
#     else:
#         return fibo(n-2)+fibo(n-1)

# print(fibo(10))

# class animal:
#     def __init__(self,name):
#         self.name = name

#     def greet(self,loud=False):
#         if loud==True:
#             print(f"HELLOOOOO {self.name}")
#         else:
#             print(f"halo {self.name}")

# g = animal('Fred')  # Construct an instance of the Greeter class
# g.greet()            # Call an instance method; prints "Hello, Fred"
# g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"          


# class Student:
#     def __init__ (self,name,varsta,nota_PEAG):
#         self.name=name
#         self.varsta=varsta
#         self.nota_PEAG=nota_PEAG
    

#     def afisare_stud(self):
#         print(f"elevul este:{self.name}, are {self.varsta} anisori si a obtinut la PEAG nota: {self.nota_PEAG}")


# newStud = Student("gigi",21,10)
# newStud.afisare_stud()



# a = np.array([1, 2, 3])  # Create a rank 1 array
# print(type(a), a.shape, a[0], a[1], a[2])
# a[0] = 5                 # Change an element of the array
# print(a)  

# b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
# print(b)

# print(b.shape)
# print(b[0, 0], b[0, 1], b[1, 0])

# a = np.zeros((2,2))  # Create an array of all zeros
# print(a)

# b = np.ones((1,2))   # Create an array of all ones
# print(b)
# print(type(b[0, 0])) # While numbers in Python are integer by default, numpy's default is double. Seems familiar?

# c = np.full((2,2), 7) # Create a constant array
# print(c)




# # Create the following rank 2 array with shape (3, 4)
# # [[ 1  2  3  4]
# #  [ 5  6  7  8]
# #  [ 9 10 11 12]]
# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# # Use slicing to pull out the subarray consisting of the first 2 rows
# # and columns 1 and 2; b is the following array of shape (2, 2):
# # [[2 3]
# #  [6 7]]
# b = a[:2, 1:3]
# print(b)

# Create the following rank 2 array with shape (3, 4)
# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(a)

# row_r1 = a[1, :]    # Rank 1 view of the second row of a  
# row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
# row_r3 = a[[1], :]  # Rank 2 view of the second row of a
# print(row_r1, row_r1.shape)
# print(row_r2, row_r2.shape)
# print(row_r3, row_r3.shape)

# # We can make the same distinction when accessing columns of an array:
# col_r1 = a[:, 1]
# col_r2 = a[:, 1:2]
# print(col_r1, col_r1.shape)
# print()
# print(col_r2, col_r2.shape)

# a = np.array([[1,2], [3, 4], [5, 6]])

# # An example of integer array indexing.
# # The returned array will have shape (3,) and 
# print(a[[0, 1, 2], [0, 1, 0]])

# # The above example of integer array indexing is equivalent to this:
# print(np.array([a[0, 0], a[1, 1], a[2, 0]]))


