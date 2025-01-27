def fact(n):
    if n==0:
        return 1
    f=n*fact(n-1)
    #print(f)
    return f

print(fact(5))
