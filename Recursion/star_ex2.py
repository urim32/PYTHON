
list1 = [2, 3, 99, 22, 444, 11111, 4]


def find_max(nums):
    if len(nums) == 0:
        return nums
    elif len(nums) == 1:
        return nums[0]
    i = len(nums)
    if nums[i-1] >= nums[i-2]:
        nums.remove(nums[i-2])
    elif nums[i-2] > nums[i-1]:
        nums.remove(nums[i-1])
    return find_max(nums)


x = find_max(list1)
print(x)
