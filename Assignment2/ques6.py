# Find LCM

num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
lcm = 0
if num1>num2:
    lcm = num1
else :
    lcm = num2 

while True:
    if lcm%num1==0 and lcm%num2==0:
        print(lcm)
        break
    lcm+=1 