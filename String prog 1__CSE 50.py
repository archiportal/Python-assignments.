def palindrome(str):
    reverse=str[::-1]
    if reverse==str:
        return True
    else:
        return False


str=input("Enter a word to see if it is a palindrome or not :")
r=palindrome(str)

if r==True:
    print(str + " is a palindrome.")
else:
    print(str + " is not a palindrome.")


