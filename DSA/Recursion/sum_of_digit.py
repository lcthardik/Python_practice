def sod(n):
    if n//10==0:
        return n
    return n%10+sod(n//10)

print(sod(12345))