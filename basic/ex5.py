# Python Program for Compound Interest
"""
A = P(1 + R/100) t
Compound Interest = A – P
Where,
A is amount
P is the principal amount
R is the rate and
T is the time span
"""

def compoudintrest(p,t,r):
    print("the principal amount is" , p)
    print("the intrest rate is" , r)
    print("the time span is", t)

    a=p*(1+(r/100))**t
    ci=a-p

    print("the compound intrest is",ci)

P=input("enter the principal amount ")
T=input("enter the time")
R=input("enter the intrest rate")

compoudintrest(int(P),int(T),int(R))
