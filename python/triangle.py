def main():
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")
    if a == b and b == c and c == a:
   		print("Equilateral Triangle")
    elif a == b or b == c or c == a:
    	print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

if __name__ == '__main__':
    main()