'''
Check if a number is a palindrome. 
'''

n = int(input("Enter number : "))
original = n
def rev(n, result =0):
    if n==0:
        return result
    return rev(n//10,(result*10 + n%10))
if rev(n)==original:
    print("Number is palindrome")
else:
    print("Number isn't palindrome")