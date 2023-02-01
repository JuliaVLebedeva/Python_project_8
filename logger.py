from data_create import name_data, surname_data, phone_data, adress_data

def input_date():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком варианте записать данные?\n\n"
                    f"1 вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n"
                    f"2 вариант:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        var = int(input("Еще один шанс! Ваш выбор: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')
    else:
       with open('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f"{name};{surname};{phone};{adress}\n\n")

    print('Успешно!')

def print_date():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
        data_first = file.readlines()
        data_first_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_second.append(''.join(data_first[j:i]))
                j = i
        data_first = data_first_second
        print(''.join(data_first_second))
    
    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def put_date():
    data_first, data_second = print_date()
    number_file = int(input('В каком файле вносим изменения? Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        number_file = int(input('Еще один шанс! Ваш выбор: '))

    if number_file == 1:
        number_journal = int(input('Какую запись нужно изменить? Введите номер записи: '))
        number_journal -= 1
        print(f'Изменяем данную запись:\n{data_first[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        adress = adress_data()
        data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{adress}\n'] + \
                     data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Успешно!')
    else:
        number_journal = int(input('Какую запись нужно изменить? Введите номер записи: '))
        number_journal -= 1
        print(f'Изменяем данную запись:\n{data_second[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        adress = adress_data()
        data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{adress}\n'] + \
                      data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Успешно!')


def delete_date():
    data_first, data_second = print_date()
    number_file = int(input('В каком файле вносим изменения? Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        number_file = int(input('Еще один шанс! Ваш выбор: '))

    if number_file == 1:
        number_journal = int(input('Какую запись нужно удалить? Введите номер записи: '))
        print(f'Удаляем данную запись:\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Успешно!')
    else:
        number_journal = int(input('Какую запись нужно удалить? Введите номер записи: '))
        print(f'Удаляем данную запись:\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Успешно!')