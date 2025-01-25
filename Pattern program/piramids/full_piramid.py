def full_piramid(n):
    for row in range(n):
        #half reverse left
        for col in range(row,n):
              print(' ', end="")
        #half left
        for col in range(row+1 ):
              print(col, end=" ")
        print("")


# Example: Print a half pyramid with 5 rows
n = int(input("enter a number : "))
full_piramid(n)