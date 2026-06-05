'''
Count how many elements are common between two arrays. 
'''

m = int(input("Enter m : "))
arr1 = []
for i in range (m):
    arr1.append(int(input("Enter Element : ")))
print(arr1)
n = int(input("Enter n : "))
arr2 = []
for i in range (n):
    arr2.append(int(input("Enter Element : ")))
print(arr2)
count = 0
for x in arr1:
    if x in arr2:
        count+=1
print("Count of Common elements between two array is",count)
