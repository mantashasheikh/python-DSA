# Sum of First and Last Digit of a Number
num = int(input("enter a number : "))
last = num%10
while num>=10:
    num = num//10
first = num
print("sum = ", first+last)
    