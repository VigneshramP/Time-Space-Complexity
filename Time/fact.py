def factorial(num):
	if num == 1:
		return num
   
   	else:
   		return num * factorial(num - 1)

def main():
	print "<===== Factorial Program =====>\n"
	num = int(input("Enter the Value\n"))
	
	if num < 0:
		print "Sorry, factorial does not exist for negative numbers"

	elif num == 0:
		print "The factorial of 0 is 1"

	else:
		print "The factorial of {} is : ".format(num),factorial(num)

if __name__ == '__main__':
       	main()       

