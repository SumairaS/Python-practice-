"""
Write a program that determines whether a given year is a leap year or not. (A leap year is divisible by 4, except for years that are divisible by 100 but not by 400.)
"""
y=int(input("Enter the year:"))
if(y%4==0 or (y%100==0 and y%400!=0)):
    print(f"{y} is a leap year")
else: 
    print(f"{y} is not a leap year")
