'''
Replace all occurrences of a character (say ‘a’ → ‘x’) recursively. 
'''

s = input("Enter string : ")
def rep(s,i=0):
    if i==len(s):
        return ""
    if s[i] == "a":
        return "x" + rep(s,i+1)
    else:
        return s[i] + rep(s,i+1)

print(rep(s))