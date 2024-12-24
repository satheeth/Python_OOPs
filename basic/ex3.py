'''
num = 7

fact = 1
if num<0:
    print("itz negative number")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of ",num, "is",fact)
'''
'''
Here, the number whose factorial is to be found is stored in num, and we check if the number is negative,
zero or positive using if...elif...else statement. If the number is positive, we use for loop and range()
function to calculate the factorial.

iteration	factorial*i (returned value)
i = 1	1 * 1 = 1
i = 2	1 * 2 = 2
i = 3	2 * 3 = 6
i = 4	6 * 4 = 24
i = 5	24 * 5 = 120
i = 6	120 * 6 = 720
i = 7	720 * 7 = 5040
'''
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return (n*factorial(n-1))
num= 4
print("factorial of ",num, "is",factorial(num))
'''