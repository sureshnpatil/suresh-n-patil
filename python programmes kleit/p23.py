# Program to Print X shape inside Hollow Square

n=int(input("Enter the number of lines: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
        elif i == j or i == n-j-1:
                print("*", end=" ")
        else:
                print(" ", end=" ")
    print()