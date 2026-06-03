'''
Compare two arrays — check if they contain the same elements (ignore order). 
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
if set(arr1) == set(arr2):
    print("They contain the same elements (ignore order)")
else:
    print("They doesn't contain the same elements")