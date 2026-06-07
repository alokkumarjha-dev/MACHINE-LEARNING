'''
Create a frequency array of numbers (count occurrence of each number).
'''

n = int(input("Enter n : "))
arr = []
for i in range (n):
    arr.append(int(input("Enter Element : ")))
print(arr)
freq = {}
for x in arr:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
print(freq)