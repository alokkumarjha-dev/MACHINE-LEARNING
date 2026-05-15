'''
Print the product of digits of a given number.
'''

n = int(input("Enter n : "))
product=1
while n>0:
    digit = n%10
    product *= digit
    n//=10
print("Product of digit is ",product)