'''
Calculate the sum of first n even numbers recursively. 
'''

n = int(input("Enter number : "))
def soe(i,n):
    if i>n:
        return 0
    elif i%2==0:
        return i + soe(i+1,n)
    else:
        return soe(i+1,n)
print(soe(1,n))