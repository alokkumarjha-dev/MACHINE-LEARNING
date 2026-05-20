'''
Remove all spaces from a string recursively.
'''

s = input("Enter string : ")
def spaces(s,i=0):
    if i==len(s):
        return ""
    if s[i]== " ":
        return spaces(s,i+1)
    else:
        return s[i] + spaces(s,i+1)
print(spaces(s))