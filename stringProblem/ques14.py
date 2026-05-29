# Q.15 W.A.P TO DELETE VOWELS FROM STRING?
s = input("enter a string : ")
result = ""
for ch in s : 
    if ch not in "aeiouAEIOU":
        result += ch
print(result)        
    