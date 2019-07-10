def palindrome(st):
    n = len(st)
    if n == 0:
        return True
    elif n == 1:
        return True
    elif st[0] == st[n-1]:
        st = st[1: -1]
        return palindrome(st)
    else:
        return False


string = "12321"
x = palindrome(string)
print(x)
