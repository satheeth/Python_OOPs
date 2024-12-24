# Python Program to Check Prime Number
num=int(input("enter the number  greater than of 2"))
for i in range(2,num):
    if num % i == 0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is prime number")