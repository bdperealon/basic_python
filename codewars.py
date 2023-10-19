import re


def disemvowel(string_):
    return re.sub("[AEIOUaeiou]", "", string_)


# In this kata you will create a function that takes a list of non-negative integers and strings
# and returns a new list with the strings filtered out.
def filter_list(list_):
    new_list = []
    for item in list_:
        if type(item) is int and item >= 0:
            new_list.append(item)
    return new_list


def main():
    print("Hello World!")
    print(disemvowel("Hello World!"))
    print(filter_list([-1, 1, "a", 2, -2, "b", "c", 3, -3, -555, 666]))


if __name__ == "__main__":
    main()
