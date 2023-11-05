"""
Your module description
"""
f1=open("rose.jpg",'rb')
f2=open("newpic.jpg",'wb')
bytes=f1.read()
f2.write(bytes)
print("new img is avialbel with the namwe newpic.jpg")
