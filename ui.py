from logger import input_date, print_date, put_date, delete_date

def interface():
    print('Добрый день! Это бот-помощник. \n'
    'Что Вы хотите сделать?\n'
    '1 - Записать данные\n'
    '2 - Вывести данные\n'
    '3 - Изменить данные\n'
    '4 - Удалить данные\n')

    command = int(input("Ваш выбор: "))

    while command < 1 or command > 4:
        command = int(input("Ещё один шанс! Ваш выбор: "))

    if command == 1:
        input_date()
    elif command == 2:
        print_date()
    elif command == 3:
        put_date()
    else:
        delete_date()