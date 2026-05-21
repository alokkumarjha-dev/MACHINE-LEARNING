'''
Create a new array containing squares of all numbers. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print("Original array =",arr)
new_arr=[]
for n in arr:
    new_arr.append(n**2)
print("Modified array =",new_arr)