'''
Print the string in reverse order recursively (without using loops).
'''

s = input("Enter string : ")
def rev(s,i=1):
    if i>len(s):
        return ""
    return s[len(s)-i] + rev(s,i+1)
print(rev(s))
