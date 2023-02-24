'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.



'''
import filehandling as files
import output as out
import operations as ops
import local as l


def main():
    db_data_list = files.load_db_file()
    choice = input(l.LOCAL['initial_invitation'])
    if choice == '1':
        contact = ops.input_contact()
        db_data_list.append(contact)
    elif choice == '3':
        out.print_whole_db(db_data_list)
    elif choice == '2':
        found = ops.search_contact(db_data_list)
        if found != []:
            print(l.LOCAL['found'])
            out.print_whole_db(found)
            if len(found) > 1:
                print(l.LOCAL['too_much'])
            else:
                found_choice = input(l.LOCAL['what_next'])
                if found_choice == '1':
                    db_data_list = ops.edit_contact(db_data_list, found[0])
                elif found_choice == '2':
                    db_data_list = ops.erase_contact(db_data_list, found[0])
                else:
                    print(l.LOCAL['repeat_it'])

        else:
            print(l.LOCAL['nothing_found'])
    elif choice in 'qQйЙ':
        print(l.LOCAL['quit'])
        global flag
        flag = False
    else:
        print(l.LOCAL['wrong_input'])
    files.save_db_file(db_data_list)


flag = True

while flag:
    main()
