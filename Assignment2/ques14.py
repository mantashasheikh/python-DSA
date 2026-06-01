# Convert Decimal to Binary

# num = int(input("enter a number : "))
# binary = bin(num)
# print(binary[2:])


num = int(input("enter a number : "))
binary = ""
while num>0:
    rem = num%2
    binary += str(rem)
    num//=2
print(binary) 