'''
Print sum of first n natural numbers recursively.
'''

n = int(input("Enter n : "))

def number(n):
    if n == 0:
        return 0
    return n + number(n-1)
print(number(n))