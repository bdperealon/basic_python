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


# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to
# an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a
# Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings
# representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter
# (direction) and you know it takes you one minute to traverse one city block, so create a function that will
# return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!)
# and will, of course, return you to your starting point. Return false otherwise.

#     Note: you will always receive a valid array containing a random assortment of direction letters
#     ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
def is_valid_walk(walk):
    north_steps = 0
    south_steps = 0
    east_steps = 0
    west_steps = 0
    if len(walk) == 10:
        for step in walk:
            match step:
                case 'n':
                    north_steps += 1
                case 's':
                    south_steps += 1
                case 'e':
                    east_steps += 1
                case 'w':
                    west_steps += 1
        if (north_steps - south_steps == 0) and (east_steps - west_steps == 0):
            return True
        else:
            return False
    else:
        return False


def main():
    print("Hello World!")
    print("----------------------------------")
    print(disemvowel("Hello World!"))
    print("----------------------------------")
    print(filter_list([-1, 1, "a", 2, -2, "b", "c", 3, -3, -555, 666]))
    print("----------------------------------")
    print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
    print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
    print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))


if __name__ == "__main__":
    main()
