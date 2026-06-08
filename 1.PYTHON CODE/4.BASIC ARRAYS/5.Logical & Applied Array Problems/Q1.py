'''
Check if the array is sorted in ascending order. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
flag = True
for j in range(1,n):
    if arr[j-1]>arr[j]:
        flag = False
        break
if flag == True:
    print("Array is sorted in ascending order")
else:
    print("Array is not sorted in ascending order")
