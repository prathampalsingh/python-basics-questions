# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# 123...n

# Sample Input 
# 3

# Sample Output 
# 123

n = int(input())
for x in range(1, n+1):
    print(x, end="")