# Python Program to Find Area of a Circle

# Area = pi * r2
# where r is radius of circle

def areaofcircle(r):
    pi=3.142
    ac=pi*(r*r)
    print("the area of circle of",r,"is",ac)

R=input("enter the number to find area of circle")
areaofcircle(int(R))