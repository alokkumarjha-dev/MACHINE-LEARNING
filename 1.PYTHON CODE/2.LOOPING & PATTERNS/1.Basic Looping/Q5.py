'''
Print the table of a given number (n × 1 to n × 10).
'''

n = int(input("Enter n : "))
print("Table of " ,n)
for i in range(1,11):
    print(n,"*",i,"=",n*i)