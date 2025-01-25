def half_pyramid(n):
    for row in range(n):
        #half-left 
        for col in range(row):
            print(' ', end="")
        #half reverse left
        for col in range(row,n):
              print(col, end="") 
        if row == col:
             break
        print("")

# Example: Print a half pyramid with 5 rows
n = int(input("enter a number : "))
half_pyramid(n)