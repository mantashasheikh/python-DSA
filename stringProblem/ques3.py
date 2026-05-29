# Q.3 W.A.P TO PRINT THE STRING IN REVERSE ORDER IGNORING SPACES WITHOUT USING INBUILT
# FUNCTION?
s = input("enter a string : ")
reverse = ""
for char in range(len(s)-1 , -1, -1):
    if s[char] != " ":
        reverse += s[char]
print(reverse)        
        