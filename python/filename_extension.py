def main():
   file_name = input("Enter file name  : ")
   #print(file_name)
   f = file_name.split(".")
   print(f[-1])

if __name__ == '__main__':
    main()