# Count Even and Odd Numbers in an Array
a = [5,2,4,3,7,0,1]
even = 0
odd = 0
for i in range(len(a)):
    if a[i]%2==0:
        even+=1
    else:
        odd+=1
print(even, " : even")         
print(odd , " : odd")  