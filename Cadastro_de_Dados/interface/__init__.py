def user_age(msg_age): # SEPARA USER_AGE EM OUTRA FUNÇÃO E VOLTAR SOMENTE COM USER PARA O MENU 
    while True:
        try:
            choise_user = int(input(msg_age))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite somente os numeros inteiros válidos.\033m')
            user_name(msg_name=name)
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar nada\033[m')
            return 0 
        else:
            return choise_user

def user_name(msg_name):
    while True:
        try:
            user_name = str(msg_name)
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite seu nome sem o uso de números. ex: douglas ')
            continue 
        except(KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar nada!\033[m')
            return 0
        else:
            return user_name

def menu_header(txt):
    print('-'*42)
    print(txt.center(42))
    print('-'*42)

def menu(options_list):
    menu_header('MENU PRINCIPAL')
    counter = 1
    for item in options_list:
        print(f'\033[33m{counter}\033[m - \033[34m{item}\033[m')
        counter +=1
    print('-'*42)
    user_option = user_age('\033[32mEscolha uma das opções acima: ')
    return user_option

    