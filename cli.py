from prettycli import red, yellow
from simple_term_menu import TerminalMenu
from commands import (add_car, add_service, view_cars, view_services)
import os

def clear_screen():
    if os.name == 'posix':
        # For Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':
        # For Windows
        os.system('cls')

def start():
    clear_screen()
    print('\n')
    print(red('AUTOSERVICE APP\n'))
    options = ['Add Car', 'Add Service', 'View Cars', 'View Services', 'Exit']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if options[menu_entry_index] == 'Add Car':
        add_car()
    elif options[menu_entry_index] == 'Add Service':
        add_service()
    elif options[menu_entry_index] == 'View Cars':
        view_cars()
        input(yellow('\nPress Enter to return to the main menu...'))
    elif options[menu_entry_index] == 'View Services':
        view_services()
        input(yellow('\nPress Enter to return to the main menu...'))
    else:
        exit()

def main():
    while True:
        start()


if __name__ == '__main__':
    main()

