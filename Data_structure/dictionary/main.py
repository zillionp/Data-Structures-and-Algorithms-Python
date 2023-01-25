dict1 = {"Name": "xN3k", "x": [1, 3, 3, 7, "x"]}


def display_dict(di):
    print(di)


# accessing element using key
def access_element(d):
    print(d["x"])


# accessing element using get method
def access_using_get(d):
    print(d.get("Name"))


display_dict(dict1)
access_element(dict1)
access_using_get(dict1)
