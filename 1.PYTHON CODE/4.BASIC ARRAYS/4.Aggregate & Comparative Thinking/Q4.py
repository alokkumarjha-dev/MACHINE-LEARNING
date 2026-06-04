'''
Find the common elements between two arrays.
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
c_arr = []
for x in arr1:
    if x in arr2 and x not in c_arr:
        c_arr.append(x)
print(c_arr)
