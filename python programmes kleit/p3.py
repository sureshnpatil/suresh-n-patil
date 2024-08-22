#accept a number as input say X and define logic to get the output say Y.The input can only be 0 or 1 and the output must be 1 if input is 0 and vice versa
x=int(input("enter the value of X as Either 1 or 0 :"))
if X==0 or X==1:
   
    print("input number:",x,"output Number",y)
else:
    print("invalid input")
    
    
y=1-x
print(f"input number = {x},output number ={y}")