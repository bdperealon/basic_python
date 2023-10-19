import re


def disemvowel(string_):
    return re.sub("[AEIOUaeiou]", "", string_)


def main():
    print("Hello World!")
    print(disemvowel("Hello World!"))

if __name__ == "__main__":
    main()
