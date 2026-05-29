# TO CONVERT LOWER CASE INTO UPPERCASE WITHOUT USING INBUILT FUNCTION?
s = input("enter a string :")
result = ""
for ch in s:
    if "a"<= ch <= "z":
        result += chr(ord(ch)-32)
    else : 
        result += ch
print(result)        
            