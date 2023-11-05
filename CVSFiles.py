"""
Your module description
"""
import csv
with open("emp.csv","w",newline='') as f:
    w=csv.writer(f) #returns csv witer object
    w.writerow(["Eno","Ename","Esales","Eaddress"])
    n=int(input("Enter number of Empys"))
    for i in range(n):
        Eno=input("Enter EID")
        Ename=input("Enter Emp Name")
        Esales=input("sales")
        Eaddress=input("address")
        w.writerow([Eno,Ename,Esales,Eaddress])
print("total empys entry done")
"""
to open file
"""
import csv
f=open("emp.csv",'r')
r=csv.reader(f)
data=list(r)
for line in data:
    for word in line:
        print(word,"\t",end='')
    print()