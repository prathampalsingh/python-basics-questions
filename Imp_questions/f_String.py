# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.
# Function Description
# Complete the print_full_name function in the editor below.
# print_full_name has the following parameters:
# string first: the first name
# string last: the last name

# Sample Input 
# Ross
# Taylor

# Sample Output 
# Hello Ross Taylor! You just delved into python.

def print_full_name(first, last):
    x = f"Hello {first_name} {last_name}! You just delved into python."
    print(x)
    # Write your code here

first_name = input()
last_name = input()
print_full_name(first_name, last_name)