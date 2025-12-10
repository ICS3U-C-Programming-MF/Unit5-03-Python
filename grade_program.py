#!/usr/bin/env python3
# Created by Maximiliano Fairman
# Created on Dec 9th, 2025
# this program uses a function that takes a level
# and returns the middle percentage mark.


def calc_mark(level: str) -> int:
    mark = -1

    if level == "Level 4+":
        mark = 97  # A+
    elif level == "Level 4":
        mark = 90  # A
    elif level == "Level 4-":
        mark = 83  # A-
    elif level == "Level 3+":
        mark = 78  # B+
    elif level == "Level 3":
        mark = 74  # B
    elif level == "Level 3-":
        mark = 71  # B-
    elif level == "Level 2+":
        mark = 68  # C+
    elif level == "Level 2":
        mark = 65  # C
    elif level == "Level 2-":
        mark = 61  # C-
    elif level == "Level 1+":
        mark = 58  # D+
    elif level == "Level 1":
        mark = 55  # D
    elif level == "Level 1-":
        mark = 51  # D-
    # ...
    else:
        mark = -1  # Invalid input

    return mark


# ----- User Input -----
level_input = input("Enter the level (Level 1-, Level 1, Level 1+, ..., Level 4+): ")

result = calc_mark(level_input)

if result == -1:
    print("Invalid level entered.")
else:
    print("Middle percentage mark:", result)
