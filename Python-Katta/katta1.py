# creating a pyramind of numbers using loops 

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

# creating a star using * using loops
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

