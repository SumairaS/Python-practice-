"""
Use of operators

"""
'if and else'


name  = input("Enter your name: ")

age = float(input("Enter age: "))

if(age > 18):

    print(f"{name} is {age} years old. Eligible for voting!!")

elif(age == 18):

    print(f"{name} is {age} years old. Eligible for voting!!")

else:

    print(f"{name} is {age} years old. Not Eligible for voting!!")