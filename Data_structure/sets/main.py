str_set = {"No", "no", "the", "red", "one", "Show", "me", "the", "red", "wire"}

int_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

print(str_set)
print(int_set)

for x in str_set:
    print(x)


print("one" in str_set)

int_set.add(10)
print(int_set)

int_set.remove(10)
print(int_set)

lst = ["I", "am", "Mandalorian"]

str_set.update(lst)
print(str_set)
