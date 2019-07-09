def sum_nums(nums):
    sum_of_list = 0
    for num in nums:
        if type(num) == int:
            sum_of_list += num
    return sum_of_list


rtn = sum_nums([1, 2, "dasjh"])
print(rtn)
