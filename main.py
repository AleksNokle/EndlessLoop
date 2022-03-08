import time
import curses
from cursesmenu import *
from cursesmenu.items import *

menu = ['Continue', 'New Game', 'Settings', 'Exit']
char_menu = ['Name', 'Gender', 'Age']

def print_menu(stdscr, selected_row_idx, menu):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    main_menu = True

    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0

    # print the menu
    print_menu(stdscr, current_row, menu)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 1:
                sub(stdscr)

            # if user selected last row, exit the program
            if main_menu and current_row == len(menu)-1:
                break
            else:
                print_center(stdscr, "You selected '{}'".format(menu[current_row]))
                stdscr.getch()

        print_menu(stdscr, current_row, menu)


def sub(stdscr):
    main_menu = False
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0

    # print the menu
    print_menu(stdscr, current_row, char_menu)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:

            # if user selected last row, exit the program
            if current_row == len(char_menu)-1:
                break
            else:
                print_center(stdscr, "You selected '{}'".format(char_menu[current_row]))
                stdscr.getch()

        print_menu(stdscr, current_row, char_menu)

curses.wrapper(main)

