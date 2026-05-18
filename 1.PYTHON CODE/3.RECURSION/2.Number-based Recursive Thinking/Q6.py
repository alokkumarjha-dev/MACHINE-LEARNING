'''
Check if a number is a perfect number. 
'''

n = int(input("Enter an Number : "))
original = n
def perfnum(i,n):
    if i==n:
        return 0
    elif n%i==0:
        return i + perfnum(i+1,n)
    else:
        return perfnum(i+1, n)
if perfnum(1,n) == original:
    print(original,"is perfect number")
else:
    print(original,"is not perfect number")
