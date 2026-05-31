'''
Rotate an array by one position to the left.
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print("Original array =",arr)
new_arr = arr[1:] + [arr[0]]
print("Array by rotating one position to the left =",new_arr)

