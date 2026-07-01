'''
Count how many alphabets are before ‘m’ and after ‘m’ in a given string.
'''

x = input("Enter string : ")
before_count = 0
after_count = 0

for a in x:
    if a.isalpha():
        if a < "m" :
            before_count+=1
        elif a > "m" :
            after_count+=1
print("Count of alphabet before m is",before_count)
print("Count of alphabet after m is",after_count)


