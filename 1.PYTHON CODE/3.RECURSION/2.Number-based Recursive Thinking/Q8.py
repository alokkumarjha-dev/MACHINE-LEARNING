'''
Find GCD (HCF) of two numbers using Euclid’s algorithm recursively. 
'''

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a,b = map(int,input("Enter a and b : ").split())
print("Gcd is",gcd(a,b))

