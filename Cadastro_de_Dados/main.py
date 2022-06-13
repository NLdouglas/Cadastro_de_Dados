from interface import*
from arquivo import*
from time import sleep


datafile = 'userdata.txt'
if not file_existis(datafile):
    create_file(datafile)

while True:
    option_menu = menu(['Lista de usuarios cadastradas', 'Cadastrar dados novos', 'Acessar dados de algum usuario da lista', 'Sair do programa'])
    if option_menu == 1:
        read_file(datafile)
    elif option_menu == 2:
        menu_header('NOVO CADASTRO')
        name = user_name('Nome: ')
        age = user_age('Idade: ')
        sleep(0.6)
        print('Use as letras M(MASCUINO), F(FEMININO), O(OUTRO)')
        gender = user_gender('Gênero: ')
        register_user(datafile, name, age, gender)
    elif option_menu == 3:
        complete_data(datafile)  #mostra os dados completos
        #mostrar cada pessoa cadastrada com sua numeração
        # dando a opçao do usuario escolher algum numero assim 
        # apresentando os dados completos do usuario selecionado      
        
    elif option_menu == 4:
        print('fim')
        break
        
    else:
        print('Digite somente uma das opções acima(1, 2, 3 ou 4)')