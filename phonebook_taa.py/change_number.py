import json
import controller

path_to_db = 'db.json'
def change_number():
    name = input('Введите имя или фамилию контакта, который будем менять: ')
    with open (path_to_db, 'r', encoding='UTF8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Phone number'] = input('Новый номер телефона: ')
    with open (path_to_db, 'w', encoding='UTF8') as file:
        json.dump(data, file, indent=4)
    print('Номер успешно изменен')
    controller.user_choice()