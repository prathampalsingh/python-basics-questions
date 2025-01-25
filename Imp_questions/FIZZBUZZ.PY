# Given an integer n, for every positive integer i <= n, the task is to print,
# “FizzBuzz” if i is divisible by 3 and 5,
# “Fizz” if i is divisible by 3,
# “Buzz” if i is divisible by 5


n = int(input("enter a number: "))
x = 1

for x in range(1,n):
    if x%3==0 and  x%5==0:
        print("fizzbuzz")
    elif x%3==0:
        print("fizz")
    elif x%5==0:
        print("buzz")
    else:
        print(x)