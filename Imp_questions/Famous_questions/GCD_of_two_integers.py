a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
r = 0
if b > a:
    c = a
    a = b
    b = c

while(b >0):
    r = a%b
    a = b
    b = r

print(a)