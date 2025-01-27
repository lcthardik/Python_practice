def main():
    arr=[0,1,2,3,5,6,7,8]
    n = len(arr)
    actual = (n * (n + 1)) // 2
    print(actual)
    cur=sum(arr)
    print
    print(actual-cur)

if __name__ == "__main__":
    main()