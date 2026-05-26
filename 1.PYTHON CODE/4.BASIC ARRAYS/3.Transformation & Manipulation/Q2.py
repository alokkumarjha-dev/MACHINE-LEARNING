'''
Create a new array containing only even elements. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print("Original array =",arr)
new_arr=[]
for n in arr:
    if n%2==0:
        new_arr.append(n)
print("Modified array =",new_arr)