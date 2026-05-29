# W.A.P TO CONVERT UPPER CASE INTO LOWER CASE WITHOUT USING INBUILT FUNCTION?
s = input("enter a string :")
result = ""
for ch in s:
    if "A"<= ch <= "Z":
        result += chr(ord(ch)+32)
    else : 
        result += ch
print(result) 