
def main():
    with open('data.txt', 'w') as file:
        for i in range(10):
            file.write(str(i+1) + ' Hello, World! \n')

if __name__ == "__main__":
    main()