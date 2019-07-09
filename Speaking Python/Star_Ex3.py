def remove_adjacent(nums):
    for num in nums:
        if nums.count(num) > 1:
            nums.remove(num)
    return nums


nums = [1, 3, 1, 4, 5, 2, 3]
rtn = remove_adjacent(nums)
print("remove adjacent", rtn)


def linear_merge(list1, list2):
    list3 = []
    list3 = [*list1, *list2]
    list3.sort()
    return list3


list1 = [77, 1, 55, 2]
list2 = [4, 1, 99, 32]

new_list = linear_merge(list1, list2)
print("linear merge", new_list)
