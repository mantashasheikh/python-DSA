# Check Number is Equal to its Reverse
n = int(input("enter  a number : "))
num = n
rev = 0
while n>0:
    rem = n%10
    rev = rev*10+rem
    n //=10
if num==rev:
    print("palindrome")
else:
    print("not a palindrome")         
    
    