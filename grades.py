
"""
Develop a Python program that calculates the grade for a student based on their exam score. Use the following grading scale: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59).
"""
m=int(input("Enter total marks:"))
print("your grade is :")
if (m<=59): 
    print("F")
elif(m>=60 and m<=69):
    print("D")
    
elif(m>=70 and m<=79):
    print("C")
    
elif(m>=80 and m<=89):
    print("B")
    
elif(m>=90 and m<=100):
    print("A")
    
else: 
    print("invaled entry")