def sum_from_index(list1, i):
    if i > len(list1)-1:
        return 0
    return sum_from_index(list1, i+1) + list1[i]


list1 = [1, 2, 3, 4, 5, 6]
x = sum_from_index(list1, 3)
print(x)
