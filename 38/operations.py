def input_contact():
    contact = dict()
    print('\nВведите данные нового контакта.')
    contact['last_name'] = input('Введите фамилию: ')
    contact['first_name'] = input('Введите имя: ')
    contact['phone_number'] = input('Введите телефонный номер: ')
    return contact


def edit_contact(db_data_list, contact):
    db_data_list = erase_contact(db_data_list, contact)
    choice_dict = {'1':'last_name', '2':'first_name', '3':'phone_number'}
    choice = input('\nКакое поле вы хотите отредактировать? 1. Фамилию. 2. Имя. 3. Номер телефона: ')
    contact[choice_dict[choice]]= input('Новое значение: ')
    db_data_list.append(contact)
    return db_data_list


def erase_contact(db_data_list, contact):
    for i in range(len(db_data_list)):
        if contact == db_data_list[i]:
            db_data_list.pop(i)
    return db_data_list


def search_contact(db_data_list):
    criteria = input('\nВведите данные для поиска: ')
    found = list()
    for contact in db_data_list:
        for k, v in contact.items():
            if criteria in v:
                found.append(contact)
                break
    return found