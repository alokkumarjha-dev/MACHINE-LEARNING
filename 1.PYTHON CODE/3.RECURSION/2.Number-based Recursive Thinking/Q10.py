'''
Print digits of a number in words recursively (e.g., 123 → “one two three”). 
'''

n = int(input("Enter Number : "))
def towords(n):
    words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    if n == 0:
        return ""
    return towords(n//10) + words[n%10] + " " 
print(towords(n).strip())