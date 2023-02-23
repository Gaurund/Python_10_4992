import os
import pickle

FILE_NAME_PATH = 'db.txt'


def save_db_file(db_data_list):
    db_file = open(FILE_NAME_PATH, 'w', encoding='utf-8')
    db_file.write(str(db_data_list)) # Преобразование в строку позволяет записать данные в файл, но потом получается каша
    db_file.close()


def load_db_file():
    if not os.path.exists(FILE_NAME_PATH):
        db_file = open(FILE_NAME_PATH, 'x', encoding='utf-8')
        db_data_list = list()
    else:
        db_file = open(FILE_NAME_PATH, 'r', encoding='utf-8')
        db_data_list = db_file.read()
    db_file.close()
    return db_data_list
