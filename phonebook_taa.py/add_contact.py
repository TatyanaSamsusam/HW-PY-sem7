import json
import controller

def create_json():
    json_data = []
    with open('db.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    controller.user_choice()

def add_to_json():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone_number = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    json_data = {
        'Name': name,
        'Surname': surname,
        'Phone number': phone_number,
        'Comment': comment,
    }
    data = json.load(open('db.json'))
    data.append(json_data)
    with open('db.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('Новый контакт успешно добавлен')
    controller.user_choice()