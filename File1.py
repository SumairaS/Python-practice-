"""
Understanding Files in PY
"""
f=open("abcd.txt",'w')
list=["mon\n","tue\n","wed\n","thus\n","fri\n"]
f.write("software\n")
f.writelines(list)
print("written to the file successfully")
f.close()
