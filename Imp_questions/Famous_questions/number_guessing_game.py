# The compiler generates a random integer between 1 to 10 and store it in a variable for future references.
# If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
# Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
# And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
# Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.


import random

life = 3
print("welcome to number guessing game ")
print("You have 3 chances to gusses the number")

r_num = random.randrange(10)


for x in range (1,life+1):
    u_num = int(input("enter a number: "))
    if u_num == r_num and u_num <= 10:
        print("You guessed it correctly!")
    elif u_num > r_num and u_num <= 10:
        print("Too High!")
    elif u_num < r_num and u_num <= 10:
        print("Too Low!")
    else:
        raise ValueError("wrong input!!, it should be between 1 to 10")

print("Thank you for playing!") 
