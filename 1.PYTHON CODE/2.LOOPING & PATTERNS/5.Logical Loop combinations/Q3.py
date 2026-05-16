'''
Print all numbers that are palindromes between 1–500. 
'''


for n in range(1, 501):
    temp = n
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    if rev == n:
        print(n, "is palindrome")
