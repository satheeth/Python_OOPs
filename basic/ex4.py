# Python Program for Simple Interest

def simpleintrest(p,t,r):
    print("the princial amount is",p)
    print("the time is", t)
    print("the intrest rate", r)

    si=(p*t*r)/100

    print("the simple intrest is",si)

P=input("enter the principal amount ")
T=input("enter the time")
R=input("enter the intrest rate")

simpleintrest(int(P),int(T),int(R))