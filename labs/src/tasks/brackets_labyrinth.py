from labs.src.linked import linked as mc
import numpy as np
import re
import sys


def brackets(input_text: list[str]) -> str:
    """Finds unused parentheses and prints out how many and where"""

    # every line -> list of chars
    input_chars = [list(each_line) for each_line in input_text]

    if len(input_chars) == 0:
        return 'Where is the input?'

    # enumerate every line from stdin
    input_chars[:] = enumerate(input_chars)

    # variables to collect opening (stack) and closing (just a simple list) brackets' positions
    opening = mc.Stack()
    closing = []

    # traverse through the stdin
    for (str_num, char_line) in input_chars:

        # traverse through the line to find a parentheses
        for (pos, char) in enumerate(char_line):

            # if the opening bracket is found - push its position to the stack
            # else if the closing bracket is found and there is at least one opening bracket already in the stack -
            # pop this opening one from the stack. Else, appends position of the closing one to the list
            if char == '(':
                opening.push((str_num + 1, pos + 1))
            elif char == ')':
                if len(opening) > 0:
                    opening.pop()
                else:
                    closing.append((str_num + 1, pos + 1))
            else:
                continue

    res_opening = ''
    res_closing = ''

    if len(opening) > 0:
        if len(opening) == 1:
            res_opening = f"There is one unused opening bracket in line {opening[0].data[0]} position " \
                   f"{opening[0].data[1]}\n"
        else:
            res_opening = f"There are {len(opening)} unused opening bracket in the " \
                          f"{' and '.join(str(node) for node in opening)}\n"

    if len(closing) > 0:
        if len(closing) == 1:
            res_closing = f"There is one unused closing bracket in line {closing[0][0]} position " \
                   f"{closing[0][1]} \n"
        else:
            res_closing = f"There are {len(closing)} unused closing bracket in the " \
                          f"{' and '.join(str(node) for node in closing)}\n"

    return f'{res_opening}{res_closing}'


def path(labyrinth, start: str, finish: str, my_path: str) -> str:
    """ЭТО НЕ ПО ЗАДАНИЮ
    Tells you if you are going to find an exit from the labyrinth according to the path you give"""

    def compare(pos, lim):
        """Checks if you are going to the walls of the labyrinth"""
        if pos not in range(0, lim) or labyrinth[y_pos][x_pos] == 1:
            return "You are going the wrong way"
        elif [y_pos, x_pos] == fi:
            return "You found the exit"

    # Reads your start and finish positions (as first two numbers anywhere in the string) and your route.
    # It can be written in any way you want but must contain command words like: left, l, right, r, up, u, down, d
    reg = r'\bup\b|\bu\b|\bdown\b|\bd\b|\bleft\b|\bl\b|\bright\b|\br\b'
    st = [int(char) for char in re.findall(r'\d+', start, re.I)[:2:]]
    fi = [int(char) for char in re.findall(r'\d+', finish, re.I)[:2:]]
    route = [char.lower() for char in re.findall(reg, my_path, re.I)]

    # Current position
    y_pos, x_pos = st[0], st[1]

    # Checks if labyrinth is empty or start position is in the wall
    try:
        if labyrinth[y_pos][x_pos] == 1:
            return "Are you a victim of Philadelphia experiment?"
    except IndexError:
        return "Are you even in labyrinth?"

    # Some boundaries of the labyrinth (right and bottom)
    y_lim = np.shape(labyrinth)[0]
    x_lim = np.shape(labyrinth)[1]

    # Changes our position depending on the move we make
    for move in route:
        match move:
            case 'up' | 'u':
                y_pos -= 1
                if compare(y_pos, y_lim) is not None:
                    return compare(y_pos, y_lim)

            case 'down' | 'd':
                y_pos += 1
                if compare(y_pos, y_lim) is not None:
                    return compare(y_pos, y_lim)

            case 'left' | 'l':
                x_pos -= 1
                if compare(x_pos, x_lim) is not None:
                    return compare(y_pos, y_lim)

            case "right" | "r":
                x_pos += 1
                if compare(x_pos, x_lim) is not None:
                    return compare(y_pos, y_lim)

    # If the whole algorithm is done, but we didn't reach the exit or the wall
    if [y_pos, x_pos] != fi:
        return "Where are you?"


def scout(maze: np.array, start: list, finish: list):
    """Finds a way from the maze with Lee's algorithm. Returns list of coordinates from start to finish.
    Although prints out maze with the way

    Maze is numpy array where -1 is wall and -2 is empty space"""

    # Some boundaries of the labyrinth (right and bottom)
    y_lim, x_lim = np.shape(maze)[0], np.shape(maze)[1]
    neighbours = [[0, -1], [-1, 0], [1, 0], [0, 1]]

    # List of cells with free space
    valid_cells = np.argwhere(maze == -2)

    # Set the beginning of the wave and the starting point
    wave = 0
    maze[start[0]][start[1]] = 0

    # Copying maze to print out result
    res = np.copy(maze)

    # Doing ~waaaves~
    while True:

        # Just in the way there is no free cell around
        stop = True

        for [y, x] in valid_cells:
            if maze[y][x] == wave:
                for [y_off, x_off] in neighbours:
                    if (0 <= y + y_off < y_lim) and (0 <= x + x_off < x_lim) and (maze[y + y_off][x + x_off] == -2):
                        maze[y + y_off][x + x_off] = wave + 1
                        stop = False

        wave += 1
        if (maze[finish[0]][finish[1]] == -2) and not stop:
            continue
        elif (maze[finish[0]][finish[1]] == -2) and stop:
            print("NO WAY")
            return 0
        else:
            break

    way_out = [finish, ]
    current = finish

    # Getting the way back
    while True:
        y = current[0]
        x = current[1]

        for [y_off, x_off] in neighbours:
            if (0 <= y + y_off < y_lim) and (0 <= x + x_off < x_lim) and (maze[y + y_off][x + x_off] == maze[y][x] - 1):
                current = [y + y_off, x + x_off]
                way_out.append(current)
                break
        if current == start:
            break
        else:
            continue

    for [y, x] in way_out:
        res[y][x] = 0

    print(f"waves is\n{maze}\nres is\n{res}")

    return way_out[::-1]


if __name__ == "__main__":
    # ___________________Test for brackets()____________________
    # print("Text with parentheses: ")
    #
    # my_input = sys.stdin.readlines()
    #
    # print(brackets(my_input))

    # ____________________Test for labyrinth_____________________
    laby = np.array([[-1, -1, -1, -1, -2, -1],
                     [-1, -2, -2, -2, -2, -1],
                     [-1, -1, -2, -1, -2, -1],
                     [-1, -2, -2, -1, -1, -1],
                     [-1, -1, -2, -1, -1, -1]])

    second_maze = np.array([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
                            [-1, -2, -2, -2, -2, -2, -2, -2, -1],
                            [-1, -2, -2, -1, -1, -2, -2, -2, -1],
                            [-1, -2, -2, -1, -1, -2, -2, -2, -1],
                            [-1, -2, -2, -1, -1, -2, -2, -1, -1],
                            [-1, -2, -2, -2, -2, -2, -2, -2, -1],
                            [-1, -1, -1, -1, -1, -2, -2, -2, -1],
                            [-1, -2, -2, -2, -1, -1, -1, -2, -2],
                            [-1, -2, -1, -2, -2, -2, -2, -2, -2],
                            [-1, -1, -1, -1, -1, -2, -2, -2, -2]])

    starting = [0, 4]
    finishing = [4, 2]
    # my_start = input("Your start point: ")
    # my_finish = input("Your exit from the labyrinth: ")
    # da_way = input("Your path: ")

    # scout(laby, starting, finishing)

    print(scout(second_maze, [1, 1], [7, 2]))

    """
    OUTPUT FOR scout()
    
    waves is
    [[-1 -1 -1 -1 -1 -1 -1 -1 -1]
     [-1  0  1  2  3  4  5  6 -1]
     [-1  1  2 -1 -1  5  6  7 -1]
     [-1  2  3 -1 -1  6  7  8 -1]
     [-1  3  4 -1 -1  7  8 -1 -1]
     [-1  4  5  6  7  8  9 10 -1]
     [-1 -1 -1 -1 -1  9 10 11 -1]
     [-1 -2 19 18 -1 -1 -1 12 13]
     [-1 -2 -1 17 16 15 14 13 14]
     [-1 -1 -1 -1 -1 16 15 14 15]]
    res is
    [[-1 -1 -1 -1 -1 -1 -1 -1 -1]
     [-1  0 -2 -2 -2 -2 -2 -2 -1]
     [-1  0 -2 -1 -1 -2 -2 -2 -1]
     [-1  0 -2 -1 -1 -2 -2 -2 -1]
     [-1  0 -2 -1 -1 -2 -2 -1 -1]
     [-1  0  0  0  0  0 -2 -2 -1]
     [-1 -1 -1 -1 -1  0  0  0 -1]
     [-1 -2  0  0 -1 -1 -1  0 -2]
     [-1 -2 -1  0  0  0  0  0 -2]
     [-1 -1 -1 -1 -1 -2 -2 -2 -2]]
     
[[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [6, 5], [6, 6], [6, 7], [7, 7], [8, 7], [8, 6], [8, 5], [8, 4], [8, 3], [7, 3], [7, 2]]
 """
