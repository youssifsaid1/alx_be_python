# Pattern Drawing using nested loops

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the square pattern
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to next row
    row += 1
