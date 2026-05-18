'''
Check if a number is an Armstrong number. 
'''

n = int(input("Enter an Number : "))
original = n
x = len(str(n))
def armstrong(n):
    if n == 0:
        return 0
    return (n%10)**x + armstrong(n//10)
if armstrong(n) == original:
    print(original,"is an armstrong number")
else:
    print(original,"is not an armstrong number")