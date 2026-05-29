# W.A.P TO EXTRACT NUMBERS FROM STRING?
s = input("enter a string  : ")
result = ""
for ch in s:
    if chr(48) <= ch <=chr(57):
        result += ch
print(result)        