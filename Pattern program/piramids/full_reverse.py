def half_pyramid(n):
    for row in range(n):
        #half-left 
        for col in range(row):
            print(' ', end="")
        #half reverse left with n - 1 so the next for loop can complete the bottom 4
        for col in range(row,n-1):
              print(col, end="")
        #half reverse left
        for col in range(row,n):
              print(col, end="")
        print("")

# Example: Print a half pyramid with 5 rows
n = int(input("enter a number : "))
half_pyramid(n)