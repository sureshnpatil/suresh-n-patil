#program to find biggest (smallest) digit in a number 


input_num=input("Enter the number to find biggest digit :")
big_dig='0'
for i in input_num:
    if int(i)>int(big_dig):
        #big_num=i
        big_dig =i
print(f"The biggest input number  {input_num} is {big_dig}")