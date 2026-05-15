'''
Print the sum of all odd numbers up to n.
'''

n = int(input("Enter n : "))
sum=0
for i in range(1,n+1,2):
    sum+=i
print("Sum of all odd number upto",n,"is",sum)