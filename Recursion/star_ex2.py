

# def find_max(nums):
#     if len(nums) == 0:
#         return nums
#     elif len(nums) == 1:
#         return nums[0]
#     i = len(nums)
#     if nums[i-1] >= nums[i-2]:
#         nums.remove(nums[i-2])
#     elif nums[i-2] > nums[i-1]:
#         nums.remove(nums[i-1])
#     return find_max(nums)


# x = find_max(list1)


# better way to find max
def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]


list1 = [2, 3, 99, 22, 444, 11111, 4]

x = Max(list1)
print(x)
