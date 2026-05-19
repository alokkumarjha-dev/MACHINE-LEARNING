'''
Print a triangle of stars recursively (bottom-up).
'''

n = int(input("Enter n : "))
def star(i,n):
    if i>n:
        return ""
    return star(i+1,n) + "*"*i + "\n"
print(star(1,n))
