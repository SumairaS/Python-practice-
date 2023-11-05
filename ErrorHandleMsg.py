"""
Throwing the class of Error 
"""
try:

    a="Hello"+20

    x=int(input("Enter first number:"))

    y=int(input("Enter second number:"))

    print(x/y)

except (ZeroDivisionError,ValueError,TypeError) as msg:

    print(msg.__class__,msg)