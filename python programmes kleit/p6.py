#Program to check if the alphabet is uppercase
# Input from the user
alphabet = input("Enter an alphabet: ")

# Check if the alphabet is uppercase
if alphabet.isupper():
    print(f"{alphabet} is an uppercase letter.")
else:
    print(f"{alphabet} is not an uppercase letter.")