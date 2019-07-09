def analyze_number_digits():
    num = input("enter your number: ")
    print(f"your number is: {num}")
    str_num = str(num)
    sum = 0
    print("The digits of this number are:", end=" ")
    for i in range(len(str_num)):
        sum += int(str_num[i])
        print(str_num[i], end=",")
    print("")
    print("The sum of the digits is: ", sum)


analyze_number_digits()
