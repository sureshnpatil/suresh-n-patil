
# Program to check if a number is Perfect Square

number = int(input("Enter a number: "))
i = 1
while number > 0:
    number -= i
    i += 2
if number == 0:
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")