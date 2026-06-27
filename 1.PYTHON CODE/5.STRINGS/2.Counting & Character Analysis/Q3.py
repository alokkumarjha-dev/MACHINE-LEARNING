'''
Count how many uppercase and lowercase letters a string has. 
'''

x = input("Enter string : ")
u_count = 0
s_count = 0
for i in range(len(x)):
    if x[i].isalpha():
        if x[i].isupper():
            u_count+=1
        else:
            s_count+=1
print("Count of uppercase letters :",u_count)
print("Count of lowercase letters :",s_count)

