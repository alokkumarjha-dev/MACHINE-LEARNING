'''
Print the sum of all odd digits and even digits separately in a number. 
'''

n = int(input("Enter n : "))
se = 0
so = 0
for i in range(1,n+1):
    digit = n%10
    if digit%2==0:
        se+=digit
    else:
        so+=digit
    n//=10
print("Sum of even digits is",se)
print("Sum of odd digits is",so) 