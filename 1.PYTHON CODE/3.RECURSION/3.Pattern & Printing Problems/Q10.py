'''
Print pattern of characters (A, AB, ABC, ...) recursively. 
'''
n = int(input("Enter n : "))

def abc(i, n):
    if i > n:
        return
    print("".join(chr(65 + x) for x in range(i)))
    abc(i + 1, n)

abc(1, n)

    