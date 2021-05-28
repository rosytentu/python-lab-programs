#Generate a random number 1 and 10.Ask the user to guess the number and print a message based on whether they get it right or not.
import random
n=random.randint(0,11)
v=int(input("enter your guessed number: "))
if(n==v):
	print("your guessed number is right")
else:
		print("the guessed number is wrong")
print('n',n)
