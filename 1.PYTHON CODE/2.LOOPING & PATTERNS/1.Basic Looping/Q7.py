'''
Print the sum of all even numbers up to n.
'''

n = int(input("Enter n : "))
sum=0
for i in range(2,n+1,2):
    sum+=i
print("Sum of all even number upto",n,"is",sum)