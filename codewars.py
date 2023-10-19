import re


def disemvowel(string_):
    return re.sub("[AEIOUaeiou]", "", string_)


def filter_list(list):
    new_list = []
    for item in list:
        if type(item) == type(1) and item > 0:
            new_list.append(item)
    return new_list


def main():
    print("Hello World!")
    print(disemvowel("Hello World!"))
    print(filter_list([-1, 1, "a", 2, -2, "b", "c", 3, -3]))


if __name__ == "__main__":
    main()
