from operator import truediv


def main():
    # Opens file containing input
    garbage = open(
        "C:/Users/Wyatt/Documents/github/advent-of-code-2023/Day1/input.txt", "r")

# Turns input into list
    garbage_list = garbage.readlines()
    int_list = []
    value_list = []

# iterates over every entry in the list and adds to int list if conversion to integer is successful
    for entry in garbage_list:
        for c in entry:
            try:
                int(c)
                value_list.append(c)
            except:
                continue
        int_list.append("".join(value_list))
        value_list.clear()

# Joins every the first and last integer from the valuesin the list and then sums all the integers
    sum = 0
    print(len(int_list))
    for i in range(0, len(int_list),):
        value = int_list[i][0:1] + \
            int_list[i][len(int_list[i]) - 1:len(int_list[i])]
        sum += int(value)
    print(sum)


if __name__ == "__main__":
    main()
