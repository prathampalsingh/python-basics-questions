def half_diamond(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
              print("* ", end="")     #*****
              #print(row, end="")     #55555
              #print(col, end="")     #12345
        print("")
    for row in range(n,0,-1):
        for col in range(1, row ):
              print("* ", end="")
        print("")


# Example: Print a half pyramid with 5 rows
n = int(input("enter a number : "))
half_diamond(n)