'''
Find the smallest and largest digit in a given number. 
'''

n = int(input("Enter Number : "))
smallest = 9
largest = 0
temp = n
while temp>0:
    digit = temp%10
    if digit>largest:
        largest = digit
    if digit<smallest:
        smallest = digit
    temp//=10
print("Largest is",largest)
print("Smallest is",smallest)
