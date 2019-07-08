# 1
for i in range(1, 41):
    print(i)
# 2
i = 1
while i <= 40:
    print(i)
    i = i+1
# 3


def print_fuzz_buzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        print(num)


print_fuzz_buzz()
