#  1.     Write a program to Python find the values which************************************************
#   is not divisible 3 but is should be a multiple of 7.
#    Make sure to use only higher order function.

# normal way...........................
# def func(num):
#     if num%3!=0 and num%7==0:
#         return True
#     else:
#         return False
# print(func(7))

# lambda..................................
test=lambda x: x if (x%3!=0 and x%7==0) else False
print(test(3))
print(test(7))
print(test(24))




# 2.    Write a program in Python to multiple the element of list*************************************************
#  by itself using a traditional function and pass the function to map to complete the operation.

# normal method..............................
# l=[1,2,3,4,5,6,7,8]
# def func(l):
#     for i in l:
#         print(i*i) 
# func(l)

# by using map function.
mylist=[1,2,3,4,5,6,7,8]
def multiple(x):
    return x * x
   
print(list(map(multiple,mylist))) 



# 3.    Write a program to Python find out the character ******************************************
# in a string which is uppercase using list comprehension.

# normal method.....................
# str="Satish Hiru Gadge"
# for i in str:
#     if i.isupper():
#         print(i,end="")

# List Comprehension................
str="Satish Hiru Gadge"
res=[i for i in str if i.isupper()]
print(res)



#  4.Write a program to construct a dictionary from *****************************************************
# the two lists containing the names of students and 
# their corresponding subjects. The dictionary should 
# maps the students with their respective subjects. 
# Let’s see how to do this using for loops and dictionary comprehension. 
# HINT-Use Zip function also
# ● Student = [&#39;Smit&#39;, &#39;Jaya&#39;, &#39;Rayyan&#39;]
# ● capital = [&#39;CSE&#39;, &#39;Networking&#39;, &#39;Operating System&#39;]

Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']
d=(dict(zip(Student,capital)))
print(d)
print(type(d))




# 5. Learn More about Yield, next and Generators********************************************************

# The yield keyword, unlike the return statement, is
#  used to turn a regular Python function in to a generator.

# finding the cube  using the normal terms is done as below.....................
# def cube_numbers(nums):
#     cube_list =[]
#     for i in nums:
#         cube_list.append(i**3)
#     print(cube_list)

# cube_numbers([1, 2, 3, 4, 5])

# the same can be done using the yeild.........................................
# def cube_numbers(nums):
    
#     for i in nums:
#         yield(i**3)
    
# x=cube_numbers([1, 2, 3, 4, 5])
# print(x)    # will return the generator.
# print(list(x)) #generator is converted into list.

# NEXT ----...........
# The next() function returns the next item in an iterator.

# lis=iter(["satish","hiru","gadge"])
# print(next(lis))
# print(next(lis))
# print(next(lis))

# GENERATORS...................................................
# if we want to print the list it gives the chunk of data
# l=[1,2,3,4,5]
# in list it willprint all the numbers at once which will kill lot of memory space.
# but in case of the generator it will print one by one 
# for example it will first print 1 and then it will print 2 only after our demand.
# this is how the memory space is saved.

# example of generator.
# Thcommon example to print the number from 1 to 10
# def func():
#     for i in range(1,11):
#         print(i)
# func()

# lets create a generator using the same example
# def func():
#     for i in range(1,11):
#         yield(i)
# print(func())
# this gives the output as generator.
# for j in func():
#     print(j)

# for j in func():
#     print(j)

# for j in func():
#     print(j)

# for j in func():
#     print(j)

# for j in func():
#     print(j)
# I have applied the for loop for the 5 times but it is giving
# the generator 1 time only ...behind the scene when we demand
# for the second time it delete the first one and it goes so on.
# if we try to do this with list it will print the list 5 times.



# 6. Write a program in Python using generators to**********************************************************
#  reverse the string. Input String = 
# “Consultadd Training”

# By using the normal terms...................................
# str=
# print(str[::-1])

# by using generator ........................................

def rev_str(name):
    for i in range (len(name) - 1, -1, -1):
        yield name[i]
for i in rev_str('Consultadd Training'):
    print(i ,end="")

    

#  7.    Write any example on decorators.*****************************************************************

# Decorator.............................................
# Decorator is a function that enhance the functionality of another function.

# def my_decorator(func):
#     def wrapper():
#         print("I am in INDIA!!!")
#         func()
#         print("I came to USA!!!")
#     return wrapper

# def say_wee():
#     print("Whee!!!")

# x=my_decorator(say_wee)
# x()



# 8.    Write a program to handle an error if the user ****************************************************
# entered the number more than
# four digits it should return 
# “Please length is too short/long !!! Please provide only four
# digits”

    
# try:
#     x= int(input("Please enter a digit : "))   
#     if len(str(x))>4 or len(str(x))<3:    # TypeError: object of type 'int' has no len()  but we havw to take the input in integer.
#         print("Please length is too short/long !!! Please provide only four digits ")
#     else:
#         print("Perfect!!!")    
# except:
#     print("Alphabets are not allowed!!!")



# 9.    Create a login page backend to ask user to enter the UserEmail and password.*******************************
# Make sure to ask Re-Type Password and if the password is incorrect give chance to
# enter it again but it should not be more than 3 times.


# print('Enter correct username and password to login!!!')
# count=0
# while count < 3:
#     username = input('Enter username: ')
#     password = input('Enter password: ')
#     if username=='satish' and password=='14':
#         print('Access granted!!!')
#         count += 1
#         print(f"Congratulations!!! you have login in {count}st attempt")
#         break
        
#     else:
#         print('Access denied. Try again!!!')
#         count += 1
#     print(f"your count is {count} !!! you have 3 attempt for login ")





