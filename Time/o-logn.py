def sort(list_of_numbers):
    less = []
    equal = []
    greater = []
    #import pdb;pdb.set_trace()
    if len(list_of_numbers) > 1:

        number = list_of_numbers[0]
        for i in list_of_numbers:
            if i < number:
                less.append(i)
            elif i == number:
                equal.append(i)
            elif i > number:
                greater.append(i)
        return sort(less) + equal + sort(greater)  
    else:
        return list_of_numbers  

def main():
    print "<===== QUICK SORT =====>\n"
    num_List = []
    length = int (input("Enter the Length of List\n"))
    for i in range(length):
        num_List.append(int(input("Enter the List Values: ")))

    print "<===== SORTING LIST =====>\n"
    print sort(num_List)

if __name__ == '__main__':
    main()