import add_contact as ac
import user_interface as ui
import change_number as cn
import delete_contact as dc 
import show_all_contacts as sac
import export_to_local as el

def user_choice():
    chosen_num = ui.menu()
    if chosen_num < 0 or chosen_num > 6:
        print('Ошибка ввода. Число должно соответствовать пунктам меню')
        user_choice()
    elif chosen_num == 0:
        ac.create_json()
    elif chosen_num == 1:
        ac.add_to_json()
    elif chosen_num == 2:
        cn.change_number()
    elif chosen_num == 3:
        dc.delete_number()
    elif chosen_num == 4:
        sac.show_all_contacts()
    elif chosen_num == 5:
        el.export_txt()
    elif chosen_num == 6:
        print('Спасибо и до новых встреч!')
        exit() 
