# Python Program for n-th Fibonacci number
n=int(input("enter the number to find fibonacci series"))
a=0
b=1
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)