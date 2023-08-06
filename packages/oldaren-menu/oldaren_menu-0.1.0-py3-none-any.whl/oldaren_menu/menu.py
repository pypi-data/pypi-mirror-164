# -*- coding: utf-8 -*-

def menu(**kwargs):
    while True:
        __print_menu(**kwargs)
        selected_option = input('Please enter menu option: ').strip()
        if selected_option in kwargs:
            return kwargs[selected_option]()
        else:
            print(f'{selected_option} is invalid. Please try again.')


def __print_menu(**kwargs):
    print()
    print('MENU')
    print('-----')
    for key in kwargs:
        print(f'{key}')
    print()