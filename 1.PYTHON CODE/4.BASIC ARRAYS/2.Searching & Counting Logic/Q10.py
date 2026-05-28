'''
Count how many elements are perfect squares.
'''

n = int(input("Enter n : "))
arr = []
count = 0
for i in range (n):
    arr.append(int(input("Enter Element : ")))
    root = int(arr[i]**0.5)
    if root*root == arr[i]:
        count+=1
print(arr)
print("Count of element whic are perfect square",count)
