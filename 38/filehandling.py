import os
import pickle

FILE_NAME_PATH = 'db.txt'


def save_db_file(db_data_list):
    # db_file = open(FILE_NAME_PATH, 'w', encoding='utf-8')
    # db_file.write(str(db_data_list)) # Преобразование в строку позволяет записать данные в файл, но потом получается каша
    # db_file.close()
    with open(FILE_NAME_PATH, 'wb') as db_file:
        pickle.dump(db_data_list, db_file)
        print('\nБаза контактов сохранена')


def load_db_file():
    if not os.path.exists(FILE_NAME_PATH):
        db_file = open(FILE_NAME_PATH, 'x')
        db_data_list = list()
    else:
        db_file = open(FILE_NAME_PATH, 'rb')
        db_data_list = pickle.load(db_file)
    db_file.close()
    return db_data_list
