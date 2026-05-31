# Find HCF
num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
min = 0
if num1<num2:
    min = num1
else :
    min = num2 

hcf = 1    
for i in range(1,min+1):
    if num1%i==0 and num2%i==0:
        hcf = i
print(hcf)               