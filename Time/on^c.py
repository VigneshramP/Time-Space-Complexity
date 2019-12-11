def main():
	matrix = []
	row = int(input("Enter Row Size\n"))
	column = int(input("Enter Column Size\n"))
	for i in range(0,row):
		temp = []
		for j in range(0,column):
			temp.append(int(input("Enter the Matrix Value({}{}): ".format([i],[j]))))
		matrix.append(temp)
	for i in matrix:
		print i 		

if __name__ == '__main__':
	main()