def contact_info():
    import Menu
    import csv

    first_name = input('Введите имя ')
    family_name = input('Введите фамилию ')   
    phone = input('Введите номер телефона ')
    contact = [first_name, family_name, phone]
    with open(Menu.files_names[0], 'a+') as File:        
        File.write(' '.join(contact) + '\n')
    with open(Menu.files_names[1], 'a+') as File:        
        File.write(' '.join(contact) + '\n')
    print('Контакт "', ' '.join(contact), '" успешно добавлен!')