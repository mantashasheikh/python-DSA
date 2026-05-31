# Count Total Digits in a Number
num = int(input("entera number : "))
count = 0
while num>0:
    rem = num%10==0
    count+=1
    num = num//10
print(count)    