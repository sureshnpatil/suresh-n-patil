# Program to Accept 3 distinct numbers and find smallest among them.

input_num1 = int(input('Enter  first number: '))
input_num2 = int(input('Enter second number: '))
input_num3 = int(input('Enter  third number: '))

# check if valid input

if input_num1 < input_num2 and input_num1 < input_num3:
    print(f'{input_num1} is smallest')
elif input_num2 < input_num3:
    print(f'{input_num2} is smallest')
else:
    print(f'{input_num3} is smallest')