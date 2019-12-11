def swap(num1,num2):
	print "<===== BEFORE SWAPPING =====>\nFirst Value = {}\nSecond Value = {}".format(num1,num2)
	num1,num2 = num2,num1
	print "<===== AFTER SWAPPING =====>\nFirst Value = {}\nSecond Value = {}".format(num1,num2)
	
def main():
	print "<===== SWAPPING PROGRAM (O(1) =====>\n"
	num1 = int (input("Enter the First Number\n"))
	num2 = int (input("Enter the Second Number\n"))
	swap(num1,num2)

if __name__ == '__main__':
	main()