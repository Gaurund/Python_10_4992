import os
import sys


def import_contacts(lst):
    # with open(os.path.join(sys.path[0], 'phonebool.txt'), 'r') as data:
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        pass


def export_contacts(new_line):
    with open('phonebook.txt', 'a+', encoding='utf-8') as data:
        s = ' '.join(new_line)
        data.writelines(s+"\n")


def input_contact():
    new_contact = input('new contact: ').split()
    print(new_contact)
    export_contacts(new_contact)


def find_contact(some_string, id):
    con_to_find = input('input someone: ')


input_contact()
