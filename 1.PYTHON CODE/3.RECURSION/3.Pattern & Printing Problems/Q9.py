'''
Print sum of series 1 + 2 + 3 + ... + n recursively and display each step.
'''

n = int(input("Enter n : "))
def sum(i,n,total=0):
    if i>n:
        return 
    total+=i
    print("Step",i,":","+".join(str(x) for x in range(1,i+1)),"=",total)
    sum(i+1,n,total)
sum(1,n)