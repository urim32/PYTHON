donuts_number = int(input("enter number of donuts: "))


def donuts(count):
    if donuts_number >= 10:
        return "Number of donuts: many"
    else:
        return f"Number of donuts: {count}"


x = donuts(donuts_number)
print(x)

s = "springdsf"


def both_ends(s):
    n = len(s)
    if n < 2:
        return ""
    else:
        s = s[0:2] + s[n-2:n]
        return s


y = both_ends(s)
print(y)


def fix_start(s):
    n = len(s)
    if n == 1 or n == 0:
        return s
    else:
        new_s = "".join((s[0], s[1:].replace(s[0], "*")))
        return new_s


s_for_fix_start = "hehehe"
z = fix_start(s_for_fix_start)
print(z)
a = "hello"
b = "world"


def mix_up(a, b):
    c = "".join((a[0:2], b[2:len(b)]))
    d = "".join((b[0:2], a[2:len(a)]))
    c = d + " " + c
    return c


c = mix_up(a, b)
print(c)
