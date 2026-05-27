'''
Find the count of prime numbers in the array. 
'''

n = int(input("Enter n : "))
arr = []
prime_count=0
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
for num in arr:
    if num>1:
        is_prime = True
        for j in range(2,int(num**0.5)+1):
            if num%j==0:
                is_prime=False
                break
        if is_prime:
            prime_count+=1

print("Prime number count is an array is",prime_count)
