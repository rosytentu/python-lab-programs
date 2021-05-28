#1.2 write a program that asks the user to enter three numbers (use three separate input statements).create variables called total and average that hold the sum and average of the three numbers and print out the values of total and average 
num1=int(input('enter 1st number:'))
num2=int(input('enter 2nd number:'))
num3=int(input('enter 3rd number:'))
total=int(num1+num2+num3)
print('total=',total)
average=float((num1+num2+num3)/3)
print('average=',average)
