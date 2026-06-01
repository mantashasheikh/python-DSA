# Find Largest Number in an Array

# a = [1,3,5,78,2,9,99,65,32]
# b = sorted(a)
# print(b[-1])

a = [1,3,5,78,2,100,99,65,32]
max = 0
for i in range(len(a)):
    if a[i]>max:
        max = a[i]
print(max)                
        
