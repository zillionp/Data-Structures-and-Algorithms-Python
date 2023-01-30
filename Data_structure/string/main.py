string = "Our secrecy is our survival. Our survival is our strength"

print(string)

print(type(string))

# first character of string
def first_character(s):
    print(s[0])


def last_chr(s):
    print(s[-1])


def rev_str(s):
    print(s[::-1])


def length_of_str(s):
    print(len(s))


def check(s):
    if "our" in s:
        print("Found")


def slicing(s):
    print(s[4:7])
    print("\n")
    print(s[:8])
    print("\n")
    print(s[-40:-20])


def modification(s):
    print(s.upper())
    print(s.lower())
    print(s.strip())
    print(s.replace("our", "We"))
    print(s.split(","))


first_character(string)
last_chr(string)
rev_str(string)
length_of_str(string)
check(string)
slicing(string)
modification(string)
