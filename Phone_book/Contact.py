def contact_info():
    import Menu
    import csv

    print('\nВыберите режим ввода\n' +
          '---------------------\n' +
          'Введите "1" - построчно\n' +
          'Введите "2" - через пробел\n' +
          '---------------------\n')
    input_choice = input('Ввод: ')
    if input_choice == '1':
        first_name = input('Введите имя ')
        family_name = input('Введите фамилию ')   
        phone = input('Введите номер телефона ')
        contact = [first_name, family_name, phone]
    elif input_choice == '2':
        contact = input('Введите данные через пробел ').split()
    else:
        print('Неизвестное значение. Укажите цифру 1 или 2\n')
        ent = input('Нажмите Enter для продолжения...\n')
        contact_info()
    with open(Menu.files_names[0], 'a+') as File:        
        File.write(' '.join(contact) + '\n')
    with open(Menu.files_names[1], 'a+') as File:        
        File.write(' '.join(contact) + '\n')
    print('Контакт "', ' '.join(contact), '" успешно добавлен!')