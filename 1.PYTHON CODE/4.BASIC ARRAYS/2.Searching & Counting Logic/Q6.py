'''
Find the sum of even elements only. 
'''

n = int(input("Enter n : "))
arr = []
even_sum = 0
for i in range (n):
    arr.append(int(input("Enter Element : ")))
    if arr[i]%2==0:
        even_sum+=arr[i]
print(arr)
print("Sum of even element",even_sum)