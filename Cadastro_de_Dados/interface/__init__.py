def user_name(msg_name):
    while True:
        name_user = str(input(msg_name)).strip()
        if name_user == '':
            print('\033[31mErro: por favor, digite algum valor para o nome de usuário, seja numeros ou palavras.\033m')
        else:
            return name_user


def user_age(msg_age):
    while True:
        try:
            age_user = int(input(msg_age))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite somente os numeros inteiros para idade(EX: 25, 12, 7...).\033m')
            continue
        else:
            return age_user
    

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
    user_option = user_value('\033[32mEscolha uma das opções acima: \033[m')
    return user_option


def user_value(msg_value): # SEPARA USER_AGE EM OUTRA FUNÇÃO E VOLTAR SOMENTE COM USER PARA O MENU 
    while True:
        try:
            choise_user = int(input(msg_value))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite somente os numeros inteiros válidos.\033m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar nada\033[m')
            return 0 
        else:
            return choise_user
    