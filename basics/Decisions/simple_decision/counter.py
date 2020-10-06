
odd = 0
even = 0

print("Enter your first number.")
num1 = int(input())

print("Enter your second number.")
num2 = int(input())

print("Enter your third number.")
num3 = int(input())


if(num1 % 2 != 0):
    odd += 1
if(num1 % 2 == 0):
    even += 1

if(num2 % 2 != 0):
    odd += 1
if(num2 % 2 == 0):
    even += 1

if(num3 % 2 != 0):
    odd += 1
if(num3 % 2 == 0):
    even += 1
else:
    print("error")


print("there are {} even and {} odd numbers".format(even, odd))

