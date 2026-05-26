'''
Check if all elements in an array are unique. 
'''

n = int(input("Enter n : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter Element : ")))
print(arr)

flag = True
for x in range(n):
    e = arr[x]
    for j in range(x+1,n):
        if e==arr[j]:
            flag = False
            break
    if not flag:
        break
        
if flag:
    print("All elements in an array are unique")
else:
    print("All elements in an array are not unique")