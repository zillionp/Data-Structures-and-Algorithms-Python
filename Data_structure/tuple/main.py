str_tuple = ("They", "all", "hate", "you", "Mando", "because", "you're", "a", "legend")
int_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

print(str_tuple)
print(int_tuple)


def firt_item(t):
    print(t[0])


def last_item(t):
    print(t[-1])


def reverse_item(t):
    print(t[::-1])


firt_item(str_tuple)
last_item(int_tuple)
reverse_item(str_tuple)
