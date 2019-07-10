list1 = [1, 4, 5, 8, 3]
list2 = [3, 4, 6, 7]


def intersection_list(list1, list2):
    my_list = [number for number in list1 if number in list2]
    return my_list


x = intersection_list(list1, list2)
print(x)
