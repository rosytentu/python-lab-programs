# 3.1 use a for loop to print a triangle like the one below .Allow the user to specify how high the triangle should be .
n=int(input("enter the rows:  "))
for i in range(1,n+1):
	for j in range(1,i+1):
		print("* ",end=' ')
	print("\n")
