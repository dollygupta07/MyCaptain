def fun(l):
    n = len(l)
    max_len = 0;
    for i in range(n):
        n1 = len(l[i])
        max_len = max(n1 , max_len)
    return max_len

def main():
    lst = ["python", "C" , "Java" , "Cpp" , ]
    l = fun(lst)
    print("Longest length: " , l)

if __name__ == '__main__':
    main()