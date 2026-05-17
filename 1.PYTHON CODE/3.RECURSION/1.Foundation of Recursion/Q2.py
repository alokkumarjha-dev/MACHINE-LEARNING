'''
Print numbers from n down to 1 using recursion.
'''

n = int(input("Enter n : "))
def number(n):
    if n==0:
        return
    print(n)
    number(n-1)
number(n)