"""
Write a Python program that takes a user's age as input and prints "You are a minor" if the age is less than 18, otherwise, it should print "You are an adult."
"""
A=int(input("Enter the age:"))

if (A<18): 
    print("You are a minor")
elif(A>=18):
    print("You are an adult")
else:
     print("invalid entry")
