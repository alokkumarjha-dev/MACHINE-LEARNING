'''
Remove all occurrences of a character from a string recursively. 
'''


s = input("Enter string : ")
to_rev = input("Enter character to remove : ")
def rev(s,i=0):
    if i==len(s):
        return ""
    if s[i] == to_rev :
        return "" + rev(s,i+1)
    else:
        return s[i] + rev(s,i+1)
print(rev(s))