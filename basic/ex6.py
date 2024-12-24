# Python Program to Check Armstrong Number
# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153

num = input("enter the number")
sum = 0
temps = int(num)

while temps > 0:
    digit = temps % 10
    sum += digit**3
    temps = temps//10

if num == sum:
    print("the ",num,"is amstrong number")
else:
    print("the ",num,"is not amstrong number")