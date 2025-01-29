a = int(input("enter 1st number: "))
previous_a = a
b = int(input("enter 2nd number: "))
previous_b = b
r = 0
if b > a:
    c = a
    a = b
    b = c

while(b >0):
    r = a%b
    a = b
    b = r


lcm = (previous_a*previous_b)/a
print(int(lcm))