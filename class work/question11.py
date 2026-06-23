#Two sum 1
l = [3,2,4]
target = int(input("enter a number : "))
l2 = []
for i in range(len(l)):
    for j in range(1,len(l)):
        if l[i] + l[j] == target:
            l2.append(i)
            l2.append(j)
print(l2)            
            
            