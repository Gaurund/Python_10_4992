from local import *


def print_contact(contact):
    for k, v in contact.items():
        print(LOCAL[k], v)


def print_whole_db(db_data_list):
    for contact in db_data_list:
        print()
        print_contact(contact)
