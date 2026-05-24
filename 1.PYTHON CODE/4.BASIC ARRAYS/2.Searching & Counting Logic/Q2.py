'''
Count how many times a given element appears. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print("Array = ",arr)
x = int((input("Enter x : ")))
count = 0
for j in range(n):
    if x == arr[j]:
        count+=1
print("Count of",x,"is",count)
