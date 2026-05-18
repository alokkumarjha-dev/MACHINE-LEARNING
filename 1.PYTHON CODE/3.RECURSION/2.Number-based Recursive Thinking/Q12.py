'''
Calculate the sum of first n odd numbers recursively
'''

n = int(input("Enter number : "))
def soo(i,n):
    if i>n:
        return 0
    elif i%2!=0:
        return i + soo(i+1,n)
    else:
        return soo(i+1,n)
print(soo(1,n))