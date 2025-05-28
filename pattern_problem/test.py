N = int(input("Enter N: "))

size = 2 * N - 1  # Total number of rows and columns

for i in range(size):
    for j in range(size):
        # Find the minimum distance from any edge
        min_dist = min(i, j, size - 1 - i, size - 1 - j)
        
        # Subtract that distance from N to get the value to print
        print(N - min_dist, end=" ")
    print()
