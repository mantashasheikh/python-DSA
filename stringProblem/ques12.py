# W.A.P TO REMOVE ALL SPACES WITH “@” AMONG SENTENCE ?
s = input("enter a string : ")
result = ""
for ch in s:
    if ch == " ":
        result += "@"
    else:
        result += ch
print(result)            
        