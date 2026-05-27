'''
Find the sum of odd elements only. 
'''

n = int(input("Enter n : "))
arr = []
odd_sum = 0
for i in range (n):
    arr.append(int(input("Enter Element : ")))
    if arr[i]%2!=0:
        odd_sum+=arr[i]
print(arr)
print("Sum of odd element",odd_sum)