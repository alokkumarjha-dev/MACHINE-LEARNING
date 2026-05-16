'''
Print numbers between 1–100 whose digits add up to a multiple of 3.
'''

for i in range(1,101):
    n = i
    sod=0
    while n>0:
        digit = n%10
        sod+=digit
        n//=10
    if sod%3==0:
        print(i)
