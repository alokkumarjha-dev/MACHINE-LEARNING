'''
Input an element x — check if it exists in the array.
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print("Array = ",arr)
x = int((input("Enter x : ")))
if x in arr:
    print(x,"exist in Array")
else:
    print(x,"doesn't exist in Array")