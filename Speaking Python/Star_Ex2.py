def match_ends(words):
    counter = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[len(word)-1]:
            counter += 1

    return counter


words = ["helloh", "aa", "jhfd", "3673", "x"]
rtn_counter = match_ends(words)
print(rtn_counter)


def front_x(words):
    x_list = []

    for word in words:
        if word.startswith('x'):
            x_list.append(word)
            words.remove(word)
    x_list.sort()
    words.sort()
    sorted_and_concat = [*x_list, *words]
    return sorted_and_concat


words2 = ["ads", "xsa", "basd", "xxxeew"]
x = front_x(words2)
print(x)


def sort_last(tuples):
    new_tuples = sorted(tuples, key=lambda x: x[-1])
    return new_tuples


tuples = [(1, 7), (3, 3), (2, 5), (4, 1)]
return_tuples = sort_last(tuples)
print(return_tuples)
