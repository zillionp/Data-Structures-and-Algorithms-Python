dict1 = {"Name": "xN3k", "x": [1, 3, 3, 7, "x"]}


def display_dict(di):
    print(di)


# accessing element using key
def access_element(d):
    print(d["x"])


# accessing element using get method
def access_using_get(d):
    print(d.get("Name"))


# using dict constructor
x = dict(pass1="1234", pass2="xert3", pass3="tjeo4r")
print(x)

# len method counts the lenght of dictionary
print(len(dict1))

# displaying all the key values in dictionary
def key_only(d):
    print(d.keys())


# adding key and value in dict
dict1["pass"] = "xn3k"


def added_key(d):
    print(d.keys())


# display all values
def value_only(d):
    print(d.values())


# item method returns each item in dictionary as tuples
def dict_as_tuples(d):
    print(d.items())


# searching items in dict
def search_dict(d):
    if "Name" in d:
        print("Found")
    else:
        print("Not found")


# ------looping dict------
# returns key only
def loop1(d):
    for x in d:
        print(x)


# retuns value only
def loop2(d):
    for x in d:
        print(d[x])


# returns key only using keys method
def loop3(d):
    for x in d.keys():
        print(x)


# returns value only using values method
def loop4(d):
    for x in d.values():
        print(x)


# returns both key and value using items method
def loop5(d):
    for x, y in d.items():
        print(x, y)


access_element(dict1)
access_using_get(dict1)
key_only(dict1)
added_key(dict1)
value_only(dict1)
dict_as_tuples(dict1)
search_dict(dict1)
loop1(dict1)
loop2(dict1)
loop3(dict1)
loop4(dict1)
loop5(dict1)
