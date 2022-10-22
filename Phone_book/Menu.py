from Logger import logger

files_names = ['Phone_book.txt', 'Phone_book.csv']
file_initiation = open(files_names[0], 'a+')
file_initiation.close

def main_menu():
    from Contact import contact_info
    from Search import look_up_contact

    print('\nМеню телефонной книги \n' +
          '---------------------\n' +
          'Введите "1" - показ записей\n' +
          'Введите "2" - добавление нового контакта\n' +
          'Введите "3" - поиск контакта\n' +
          'Введите "4" - выход\n' +
          '---------------------\n')
    choice = input('Ввод: ')
    if choice == '1':
        file_initiation = open(files_names[0], 'r+')
        file_contents = file_initiation.read()
        if len(file_contents) == 0:
            print('Телефонная книга пуста.')
            ent = input('Нажмите Enter для продолжения...\n')
            main_menu()
        else:
            print(file_contents)
            file_initiation.close
            ent = input('Нажмите Enter для продолжения...\n')
            main_menu()
    elif choice == '2':
        contact_info()
        ent = input('Нажмите Enter для продолжения...\n')
        main_menu()
    elif choice == '3':
        look_up_contact()
        ent = input('Нажмите Enter для продолжения...\n')
        main_menu()
    elif choice == '4':
        print('Выход из телефонной книги')
    else:
        print('Неизвестное значение. Укажите цифру от 1 до 4\n')
        ent = input('Нажмите Enter для продолжения...\n')
        main_menu()
main_menu()
logger()