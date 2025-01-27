def main():
    arr=[1,2,3,6,9,0,11,3,0,6]
    count=arr.count(0)
    arr=[i for i in arr if i!=0]
    arr.extend([0]*count)
    print(arr)

if __name__ == "__main__":
    main()