"""
File: mystery_patches.py
------------------------
This file creates a "mystery" effect on a given DNA TextGrid.
Given a DNA TextGrid, this program creates 4 patches of this DNA TextGrid in row of 4 columns.
The first patch converts all A's to '?', the second patch converts all T's to '?',
the third patch converts all C's to '?', and the fourth patch converts all G's to '?'
"""
import sys
from TextGrid import TextGrid

N_ROWS = 1
N_COLS = 4
PATCH_SIZE = 2
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'patch1.txt'


def edit_patch(to_change):
    """
    Implement this function to edit one patch. This function loads the TextGrid and changes every
    occurrence of the to_change character to a '?'.
    :param to_change: A character that represents the letter to change for this patch (ex. A,T,C,G)
    Returns the newly generated patch
    """

    patch = TextGrid(PATCH_NAME)
    # TODO: your code here
    pah = TextGrid.blank(patch.width, patch.height)
    for x in range(patch.width):
        for y in range(patch.height):
            cell = patch.get_cell(x, y)
            if cell.value == to_change:
                cell.value = change_letr(to_change)
            pah.set_cell(x, y, cell)
    return pah

def change_letr(value):
    if value == 'A':
        return '?'
    elif value == 'T':
        return '?'
    elif value == 'G':
        return '?'
    elif value == 'C':
        return '?'

def main():
    final_grid = TextGrid.blank(WIDTH, HEIGHT)

    # TODO: your code here
    """
    cell = final_grid.get_cell(0, 0)
    pat.set_cell(2, 0, cell)
    
    cell = final_grid.get_cell(0, 1)
    pat.set_cell(2, 1, cell)
    
    cell = final_grid.get_cell(1, 0)
    pat.set_cell(3, 0, cell)
    
    cell = final_grid.get_cell(1, 1)
    pat.set_cell(3, 1, cell)

    cell = final_grid.get_cell(0, 0)
    pat.set_cell(4, 0, cell)

    cell = final_grid.get_cell(0, 1)
    pat.set_cell(4, 1, cell)

    cell = final_grid.get_cell(1, 0)
    pat.set_cell(5, 0, cell)

    cell = final_grid.get_cell(1, 1)
    pat.set_cell(5, 1, cell)

    cell = final_grid.get_cell(0, 0)
    pat.set_cell(6, 0, cell)

    cell = final_grid.get_cell(0, 1)
    pat.set_cell(6, 1, cell)

    cell = final_grid.get_cell(1, 0)
    pat.set_cell(7, 0, cell)

    cell = final_grid.get_cell(1, 1)
    pat.set_cell(7, 1, cell)

    """
    # to_change = ['A','T','C','G']
    # pat = TextGrid.blank(WIDTH, HEIGHT)
    # # for x in range(len(to_change)):
    # i = x
    # i = 0
    # final_grid = edit_patch(to_change[0])
    # for x in range(final_grid.width + 0):
    #     for y in range(final_grid.height):
    #         cell = final_grid.get_cell(x, y)
    #         pat.set_cell(x + i, y, cell)

    # i = 2
    # final_grid = edit_patch(to_change[1])
    # for x in range(final_grid.width):
    #     for y in range(final_grid.height):
    #         cell = final_grid.get_cell(x, y)
    #         pat.set_cell(x + i, y, cell)
    
    # i = 4
    # final_grid = edit_patch(to_change[2])
    # for x in range(final_grid.width):
    #     for y in range(final_grid.height):
    #         cell = final_grid.get_cell(x, y)
    #         pat.set_cell(x + i, y, cell)

    # i = 6
    # final_grid = edit_patch(to_change[3])
    # for x in range(final_grid.width):
    #     for y in range(final_grid.height):
    #         cell = final_grid.get_cell(x, y)
    #         pat.set_cell(x + i, y, cell)
    to_change = ['A','T','C','G']
    pat = TextGrid.blank(WIDTH, HEIGHT)
    i = 0
    for a in range(len(to_change)):
        final_grid = edit_patch(to_change[a])
        for x in range(final_grid.width):
            for y in range(final_grid.height):
                cell = final_grid.get_cell(x, y)
                pat.set_cell(x + i, y, cell)
        i += 2
    print(pat)

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        # command line argument to change PATCH_NAME
        PATCH_NAME = args[0]
    main()