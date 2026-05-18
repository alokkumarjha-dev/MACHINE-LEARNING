'''
Print the reverse of a given number. 
'''

n = int(input("Enter number : "))
def rev(n, result =0):
    if n==0:
        return result
    return rev(n//10,(result*10 + n%10))
print(rev(n))