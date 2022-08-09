import int_check

def start():
    greeting = 'Привет, я телефонная книга. Выбери, что будем делать: '
    print(greeting)

def menu():
    create_book = '0. Создать новую книгу'
    add_contact = '1. Добавить новый контакт'
    change_number = '2. Изменить номер телефона'
    delete_contact = '3. Удалить контакт'
    show_all_contacts = '4. Показать все контакты'
    export_to_local = '5. Выгрузить все контакты в файл'
    exit = '6. Выйти из справочника'
    print(f'{create_book}\n{add_contact}\n{change_number}\n{delete_contact}\n{show_all_contacts}\n{export_to_local}\n{exit}')
    return int_check.int_check()
