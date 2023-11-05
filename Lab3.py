"""
Inbuilt Funtions
"""

a=10
b=0B10
c=0O10
d=0xFACE
ab=1.34

e=4+8j


print(a)
print(b)
print(c)
print(d)
print(e)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(ab))
print(type(e))

f=20
g=a<f
print(g)
print(type(g))


s1='Single'
s2="Double"

s3="""firstline
second line
third line
"""
print(type(s1))
print(s3)
a="boo"
print(type(a))

A="SUMAIRA"
print(A[1])
print(A[0:4])

x=[10,20,30,40]
print(type(x))
print(x)
byt=bytes(x)
print(type(byt))

f1="milk"
f2="tea"
f3=f1+f2
print(f3)

name= input("Enter your name:")
print("Nice to meet you",name)


l=[10,6.7,'python',True]
print(l[0:3])
