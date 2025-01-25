#factorial of a number

#example input
# 5
#example output
# 1 * 2 * 3 * 4 * 5 = 120

n = int(input("enter a number: "))
fact = 1
for x in range (1,n+1):
    fact = fact*x
    print (x, end="")
    if x < n:
        print(" * ", end="")

print(" = ",fact)