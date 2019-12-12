def fibonacci(num):
    if (num <= 1):
       return num
    else:
    	return fibonacci(num - 2) + fibonacci(num - 1)

def main():
	num = int(input("Which Number Find in Fibonacci Series: \n"))
	print "\n<===== The {}th Number in Fibonacci Series =====>\n".format(num)
	fib = fibonacci(num)
	print fib

if __name__ == '__main__':
	main()