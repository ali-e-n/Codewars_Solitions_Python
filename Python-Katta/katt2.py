# check if a string is a palindrome or not using recursion

def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])
    
s = input("Enter a string: ")
if isPalindrome(s):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
