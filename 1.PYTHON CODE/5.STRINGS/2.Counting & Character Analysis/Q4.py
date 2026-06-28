'''
Find the frequency of each character in a string (without using a map)
'''

x = input("Enter string : ")
freq = {}
for a in x:
    if a in freq:
        freq[a]+=1
    else:
        freq[a]=1
print(freq)