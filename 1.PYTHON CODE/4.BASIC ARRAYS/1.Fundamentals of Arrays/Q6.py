'''
Count how many elements are positive, negative, or zero. 
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))  
print(arr)
positive = 0
negative = 0
zero = 0
for e in arr:
    if e>0:
        positive+=1
    elif e<0:
        negative+=1
    else:
        zero+=1
print("Positive count : ",positive)
print("Negative count : ",negative)
print("Zero count : ",zero)
