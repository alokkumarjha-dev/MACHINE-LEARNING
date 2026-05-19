'''
Check if a string is palindrome using recursion. 
'''

s = input("Enter string : ")
original = s
def rev(s,i=1):
    if i > len(s):
        return ""
    return s[len(s)-i] + rev(s,i+1)
if rev(s)==original:
    print("String is palidrome")
else:
    print("String is not palindrome")