#arm strong number  from 1 to 9 then 153, 370,371
#153 = 1*1*1 + 8*8*8 + 3*3*3
#370 = 3*3*3 + 7*7*7 + 0*0*0
#1634 = 1*1*1*1+ 6*6*6*6 + 3*3*3*3 + 4*4*4*4
# 3 digits = power of 3
# 4 digits = power of 4



n = int(input("enter a number: "))
check = n
sum = 0
last_digit = 0
#converts n(int) into string then with len calculate the power
order = len(str(n))

while(n>0):
    # to store the last digit eg 182 then last digit = 2 due to modular operator
    last_digit = n%10
    # last digit **(means power to ) order eg 2^3 or 2*2*2
    sum += last_digit**order
    #to divide number by 10 and round up the number by deleting float value  eg 182/10= 182 but 182//10 = 18 
    n = n//10

if sum == check:
    print("arm strong")
else:
    print("not armstrong")