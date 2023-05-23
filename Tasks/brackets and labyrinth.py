from lsq import mycollections as mc
import numpy as np
import sys


def brackets(input_text):
    # every line -> list of chars
    input_chars = [list(each_line) for each_line in input_text]

    # enumerate every line from stdin
    input_chars[:] = enumerate(input_chars)

    # variables to collect opening (stack) and closing (just a simple list) brackets' positions
    opening = mc.Stack()
    closing = []

    # traverse through the stdin
    for (num, char_line) in input_chars:

        # traverse through the line to find a parentheses
        for (pos, char) in enumerate(char_line):

            # if the opening bracket is found - push its position to the stack
            # else if the closing bracket is found and there is at least one opening bracket already in the stack -
            # pop this opening one from the stack. Otherwise, append position of the closing one to the list
            if char == '(':
                opening.push((num + 1, pos + 1))
            elif char == ')':
                if len(opening) > 0:
                    opening.pop()
                else:
                    closing.append((num + 1, pos + 1))
            else:
                continue

    if len(opening) > 0:
        if len(opening) == 1:
            print(f"There is one unused opening bracket in the {opening[0].data[0]} line in the "
                  f"{opening[0].data[1]} position\n")
        else:
            print(f"There are {len(opening)} unused opening bracket in the {opening}\n")

    if len(closing) > 0:
        if len(closing) == 1:
            print(f"There is one unused closing bracket in the {closing[0][0]} line in the "
                  f"{closing[0][1]} position\n")
        else:
            print(f"There are {len(closing)} unused closing bracket in the {closing}\n")


    def path(labyrinth, start, finish, my_path):
        me = start
        for move in my_path:
            match move:
                case "up":
                    pass
                case "down":
                    pass
                case "left":
                    pass
                case "right":
                    pass


if __name__ == "__main__":

    # Test for brackets()
    # print("Text with parentheses: ")
    #
    # my_input = sys.stdin.readlines()
    #
    # brackets(my_input)

    # Test for labyrinth

    laby = np.array([[1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1],
                    [1, 1, 0, 1, 0, 1],
                    [1, 0, 0, 1, 1, 1]])

    start = laby[0][4]
    finish = [3][1]

    my_path = input("Your path: ").split(' ')

    print(laby[1][2])
