# 3. Print Prime Numbers
n = int(input("enter a number : "))
for i in range(n+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)    
            
                  
    
                    
        