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


def main():
    db_data_list = files.load_db_file()
    choice = input(
        '\nВыберите вариант: 1. Добавить контакт. 2. Искать контакт. 3. Просмотреть существующий список контактов. Q - завершить работу: ')
    if choice == '1':
        contact = ops.input_contact()
        db_data_list.append(contact)
    elif choice == '3':
        out.print_whole_db(db_data_list)
    elif choice == '2':
        found = ops.search_contact(db_data_list)
        if found != []:
            print('\nНайдено:')
            out.print_whole_db(found)
            if len(found) > 1:
                print(
                    '\nСлишком много совпадений. Повторите поиск, чтобы получить единственный результат.')
            else:
                found_choice = input(
                    '\nЧто вы хотите сделать с найденным?\nВыберите вариант: 1. Отредактировать. 2. Удалить ')
                if found_choice == '1':
                    db_data_list = ops.edit_contact(db_data_list, found[0])
                elif found_choice == '2':
                    db_data_list = ops.erase_contact(db_data_list, found[0])
                else:
                    print('\nОпять чего-то не то нажали. Придётся начинать всё заново.')

        else:
            print('\nПо данному запросу ничего не найдено. ')
    elif choice in 'qQйЙ':
        print('\nЗавершение программы.')
        global flag
        flag = False
    else:
        print('\nНекорректный ввод. Повторите. ')
    files.save_db_file(db_data_list)


flag = True

while flag:
    main()
