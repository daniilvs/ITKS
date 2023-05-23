from collections import mycollections as mc
import numpy as np
import re
import sys


def brackets(input_text):
    """Finds unused parentheses and prints out how many and where"""

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
    """Tells you if you are going to find an exit from the labyrinth"""
    def compare(pos, lim):
        """Checks if you are going to the walls of the labyrinth"""
        if pos not in range(0, lim) or labyrinth[y_pos][x_pos] == 1:
            print('You are going the wrong way')
            return 1
        elif [y_pos, x_pos] == fi:
            print("You found the exit")
            return 0

    # Reads your start and finish positions (as first two numbers anywhere in the string) and your route.
    # It can be written in any way you want but must contain command words like: left, l, right, r, up, u, down, d
    reg = r"\bup\b|\bu\b|\bdown\b|\bd\b|\bleft\b|\bl\b|\bright\b|\br\b"
    st = [int(char) for char in re.findall(r'\d+', start, re.I)[:2:]]
    fi = [int(char) for char in re.findall(r'\d+', finish, re.I)[:2:]]
    route = [char.lower() for char in re.findall(reg, my_path, re.I)]

    # Current position
    y_pos, x_pos = st[0], st[1]

    # Checks if start position is in the wall
    if labyrinth[y_pos][x_pos] == 1:
        raise Exception('Are you a victim of Philadelphia experiment?')

    # Some boundaries of the labyrinth (right and bottom)
    y_lim = np.shape(labyrinth)[0]
    x_lim = np.shape(labyrinth)[1]

    # Changes our position depending on the move we make
    for move in route:
        match move:
            case 'up' | 'u':
                y_pos -= 1
                if compare(y_pos, y_lim) == 1:
                    return

            case 'down' | 'd':
                y_pos += 1
                if compare(y_pos, y_lim) == 1:
                    return

            case 'left' | 'l':
                x_pos -= 1
                if compare(x_pos, x_lim) == 1:
                    return

            case "right" | "r":
                x_pos += 1
                if compare(x_pos, x_lim) == 1:
                    return

    # If the whole algorithm is done, but we didn't reach the exit or the wall
    if [y_pos, x_pos] != fi:
        print('Where are you?')


if __name__ == "__main__":

    # ___________________Test for brackets()____________________
    print("Text with parentheses: ")

    my_input = sys.stdin.readlines()

    brackets(my_input)

    # ____________________Test for labyrinth_____________________
    laby = np.array([[1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1],
                    [1, 1, 0, 1, 0, 1],
                    [1, 0, 0, 1, 1, 1],
                    [1, 1, 0, 1, 1, 1]])

    my_start = input("Your start point: ")
    my_finish = input("Your exit from the labyrinth: ")
    da_way = input("Your path: ")

    path(laby, my_start, my_finish, da_way)

    print(laby[1][2])