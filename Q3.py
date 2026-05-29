'''
Replace every negative number with 0. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print("Original array =",arr)
for j in range(n):
    if arr[j]<0:
        arr[j]=0
print("Modified array =",arr)