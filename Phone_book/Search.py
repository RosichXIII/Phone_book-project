def look_up_contact():
    import Menu

    look_up = input('Введите имя для поиска: ')
    file_initiation = open(Menu.files_names[0], 'r+')
    file_contents = file_initiation.readlines()
    found = False   
    for line in file_contents:
        if look_up in line:
            print('Данные контакта:', end=' ')
            print (line)
            found = True
            break
    if  found == False:
        print(f'Контакт с именем {look_up} отсутствует')