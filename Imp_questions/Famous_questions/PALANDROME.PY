def ispalandrome(s):
    return s == s[::-1]

s = input("enter a word")
if ispalandrome(s):
    print("its palandrome")
else:
    print(" not palandrome")