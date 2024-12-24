#f = open("dummyfile.txt","x")
#f = open("dummyfile.txt","a")
#f.write("this is first line")
#f.write("second Line")
#f.write("third Line")
#f.write("Forth Line")

f = open("dummyfile.txt","r")
#print(f.read())
print(f.readline())
f = open("dummyfile.txt","r")


import os
os.remove("demofile.txt")