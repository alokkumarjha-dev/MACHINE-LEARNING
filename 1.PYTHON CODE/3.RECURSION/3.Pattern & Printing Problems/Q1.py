'''
Print a line of n stars recursively. 
'''

n = int(input("Enter n : "))
def star(i,n):
    if i>n:
        return ("")
    return "*" + star(i+1,n)
print(star(1,n))