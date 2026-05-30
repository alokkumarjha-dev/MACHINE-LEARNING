'''
Swap the first and last elements of the array. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print("Original array =",arr)
fe = arr[0]
le = arr[n-1]
arr[0] = le
arr[n-1] = fe
print(arr)