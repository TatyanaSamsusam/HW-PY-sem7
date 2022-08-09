import controller
import json

path_to_db = 'db.json'
def show_all_contacts():
    with open (path_to_db, 'r', encoding = 'UTF8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    controller.user_choice()