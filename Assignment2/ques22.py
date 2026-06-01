# Find Second Largest Element in an Array

l = [2,1,5,4,7,6,3]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]

sec_max = 0
for m in range(len(l)-1):
    sec_max = l[m]
print(sec_max)                