def merge(nums , l , mid , r):
    a = []
    b = []
    for i in range(l , mid+1):
        a.append(nums[i])
    for j in range(mid+1 , r+1):
        b.append(nums[j])
    i,j,k = 0,0,l
    while k<=r:
        if j==len(b):
            nums[k] = a[i]
            i=i+1
            k=k+1
        elif i==len(a):
            nums[k] = b[j]
            j=j+1
            k=k+1
        elif a[i]<b[j]:
            nums[k] = a[i]
            i=i+1
            k=k+1
        else:
            nums[k] = b[j]
            j=j+1
            k=k+1

def mg(nums , l , r):
    if l>=r:
        return
    mid = (l+r)//2
    mg(nums , l , mid)
    mg(nums,mid+1,r)
    merge(nums,l,mid,r)
    
def mergesrt(nums):
    n=len(nums)
    mg(nums,0,n-1)
    return nums

print(mergesrt([2,10,4,3,50]))
                                    