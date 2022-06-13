from interface import menu_header


def file_existis(nome):
    try:
        open_file = open(nome, 'rt')
        open_file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create_file(txt):
    try:
        create = open(txt, 'wt+')
        create.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo criado {txt} criado com sucesso.')


def read_file(txt):
    try:
        read = open(txt, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        menu_header('PESSOAS CADASTRAS')
        for line in read:
            personal_data = line.split(';')
            print(f'{personal_data[0].center(42)}')
    finally:
        read.close()


def register_user(datafile, name='undefined', age=0, gender='undefined'):
    try:
        add_record = open(datafile, 'at')
    except:
        print('houve um erro na abertura do arquivo')
    else:
        try:
            add_record.write(f'{name};{age};{gender}\n')
        except:
            print('houve um erro na hora de escrever os dados do usuário')
        else:
            print(f'Novo registro de {name} adicionado!')
            add_record.close()


def complete_data(data):
    data_user = open(data, 'rt')
    #search_user = str('Digite o nome da pessoa para saber os dados completos: ')
    for line in data_user:
        search_user = line.split(';')
        print(f'{search_user[0].center(42)}{search_user[1]}{search_user[2]}')
