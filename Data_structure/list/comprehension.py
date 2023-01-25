list1 = ["I", "am", "a", "Mandalorian", "Weapon", "are", "part", "of", "my", "religion"]


def comprehansion_list(original_list, string):
    return [x for x in original_list if string in x]


new_list = comprehansion_list(list1, "r")
print(new_list)


# alternative
filter_list = [x for x in list1 if "r" in x]
print(filter_list)


# looping list comprehansion
[print(x) for x in list1]
