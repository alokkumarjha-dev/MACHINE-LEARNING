'''
Reverse a string using recursion.
'''

s = input("Enter string : ")
def rev(s,i=1):
    if i > len(s):
        return ""
    return s[len(s)-i] + rev(s,i+1)
print(rev(s))