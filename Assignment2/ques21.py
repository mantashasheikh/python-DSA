# Find Smallest Number in Array

# a = [11,3,5,78,2,9,99,65,32]
# b = sorted(a)
# print(b[0])

a = [11,3,5,78,2,100,99,65,32]
min = 9
for i in range(len(a)):
    if a[i]<min:
        min = a[i]
print(min)                
        