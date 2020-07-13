
def main():
    m = input("Enter month name : ")
    if(m == 'January' or m == 'March' or m == 'May' or m == 'July' or m == 'September' or m == 'November' ):
    	print("No. of days:" , 31 ," days")
    elif(m == 'February'):
    	print("No. of days:" , 29 ," or " ,28 , " days")
    else:
    	print("No. of days:" , 30 ," days")

if __name__ == '__main__':
    main()