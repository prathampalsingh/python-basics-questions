#0,0,1,2,3,5,8

n = int(input("enter a number: "))
first = 0
second = 0
third = 1
for i in range(n+1):
    print(first)
    third = second + third
    first = second
    second = third
    
