# list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = ["I", "am", "a", "Mandalorian", "Weapon", "are", "part", "of", "my", "religion"]

# return list elements
def display_list(lst):
    for list in lst:
        print(list)


# return list in reverse order
def reverse_list(lst):
    print(lst[::-1])


# return first element in the list
def first_element(lst):
    print(lst[0])


# return last element in the list
def last_element(lst):
    print(lst[-1])


# return the items from position 3 to 6
def between_list_element(lst):
    print(lst[3:6])


# return the (-5) element but not (-2)
def between_list_element_reverse(lst):
    print(lst[-5:-2])


# returns the items from the beginning to, but NOT position 5th item
def beginning_item_from_list(lst):
    print(lst[:5])


# returns items from position 3 to end
def dispaly_till_end(lst):
    print(lst[3:])


# checks if Weapon is present in the list
def check_list_item(lst):
    if "Weapon" in lst:
        print("Weapon is in the list")
    else:
        print("Item not found")


display_list(list1)
reverse_list(list1)
first_element(list2)
last_element(list2)
between_list_element(list1)
between_list_element_reverse(list2)
beginning_item_from_list(list2)
dispaly_till_end(list1)
check_list_item(list2)
