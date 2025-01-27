def pal_check(s):
    if len(s)<=1:
        return True
    if s[0]==s[-1]:
        return pal_check(s[1:-1])
    else:
        return False

print(pal_check('abcbaa'))