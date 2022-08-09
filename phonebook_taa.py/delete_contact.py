import json
import controller

path_to_db = 'db.json'

def delete_number():
    name = input('Введите имя или фамилию контакта, который будем удалять: ')

    with open (path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]
    with open (path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('Контакт успешно удален')
    controller.user_choice()
    
