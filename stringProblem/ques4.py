# Q.4 W.A.P TO CHECK THE GIVEN STRING IS PALINDROME OR NOT?
s = input("Enter a string : ")
reverse = s[::-1]
if reverse == s:
    print("palindrome")
else:
    print("not a palindrome")    