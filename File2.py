"""
Your module description
"""
f=open("abcd.txt",'r')
data=f.read()
print(data)
f.close()

f=open("abcd.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end='')
f.close()