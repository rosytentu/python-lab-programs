#write a program that asks the user for two numbers and prints Close if the numbers are within .001 of each other and Not close otherwise.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
d = 0
if a > b :
    d = a - b
else : 
    d = b - a
if d <= 0.001 :
    print("Close")
else :
    print("Not Close")
