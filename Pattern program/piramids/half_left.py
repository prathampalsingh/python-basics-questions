# Function to print a half pyramid pattern
def half_pyramid(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            #   print("* ", end="")     #*****
              #print(row, end="")     #55555
            print(col, end=" ")     #12345
        print("")

# Example: Print a half pyramid with 5 rows
n = int(input("enter a number : "))
half_pyramid(n)