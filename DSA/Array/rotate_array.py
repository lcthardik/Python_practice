def main():
    arr=[1,2,3,4,5,6,7]
    k=2
    k=k%len(arr)
    print(arr[-k:]+arr[:-k])

if __name__ == "__main__":
    main()