# Function to print a half pyramid pattern
def half_pyramid(n):
    for row in range(n):
        for col in range(row,n):
              print(col, end="")
        print("")


# Example: Print a half pyramid with 5 rows
n = int(input("enter a number : "))
half_pyramid(n)