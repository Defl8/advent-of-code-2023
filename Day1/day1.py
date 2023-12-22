from operator import truediv


def main():
    # Opens file containing input
    garbage = open(
        "C:/Users/Wyatt/Documents/github/advent-of-code-2023/Day1/input.txt", "r")

# Turns input into list
    garbage_list = garbage.readlines()
    int_list = []

# iterates over every entry in the list and adds to int list if conversion to integer is successful
    for entry in garbage_list:
        for c in entry:
            try:
                int_list.append(int(c))
            except:
                continue

    print(int_list)


if __name__ == "__main__":
    main()
