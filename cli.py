from prettycli import red, yellow
from simple_term_menu import TerminalMenu
from commands import (
    add_car,
    add_service,
    add_car_service,
    view_cars,
    view_services,
    get_services_for_car,
    get_cars_for_service,
)
import os


def clear_screen():
    if os.name == "posix":
        # For Unix/Linux/MacOS
        os.system("clear")
    elif os.name == "nt":
        # For Windows
        os.system("cls")


def start():
    clear_screen()
    print("\n")
    print(red("AUTOSERVICE APP\n"))
    options = [
        "Add Car",
        "Add Service",
        "Add Car With Service",
        "View Cars",
        "View Services",
        "View Services For Car",
        "View Cars For Service",
        "Exit",
    ]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if options[menu_entry_index] == "Add Car":
        add_car()
    elif options[menu_entry_index] == "Add Service":
        add_service()
    elif options[menu_entry_index] == "Add Car with Service":
        add_car_service()
    elif options[menu_entry_index] == "View Cars":
        view_cars()
        input(yellow("\nPress Enter to return to the main menu..."))
    elif options[menu_entry_index] == "View Services":
        view_services()
        input(yellow("\nPress Enter to return to the main menu..."))
    elif options[menu_entry_index] == "View Services For Car":
        get_services_for_car()
        input(yellow("\nPress Enter to return to the main menu..."))
    elif options[menu_entry_index] == "View Cars For Service":
        get_cars_for_service()
        input(yellow("\nPress Enter to return to the main menu..."))
    else:
        exit()


def main():
    while True:
        start()


if __name__ == "__main__":
    main()
