a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

if a >= b  and a >= c:
    print("a is the biggest")
elif b >= a and b >= c:
    print("b is the biggest")
elif c >= a and c >= b:
    print("c is the biggest")
else:
    raise ValueError("wrong input")

