input_num=input("Enter the number to find count of digits of a number :")
count_dict=dict()
for i in input_num:
    if i in count_dict:
        count_dict[i]+=1
    else:
        count_dict[i]=1
print(f"count of each digit in {input_num}:")
for i in count_dict:
    print(f"{i}={count_dict[i]}")