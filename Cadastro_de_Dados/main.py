from interface import*
#from arquivo import*
from time import sleep


'''datafile = 'userdata.txt'
if not file_existis(datafile):
    create_file(datafile)'''

while True:
    option_menu = menu(['Lista de usuarios cadastradas', 'Cadastrar dados novos', 'Acessar dados de algum usuario da lista', 'Sair do programa'])
    if option_menu == 1:
        read_file(datafile)
    elif option_menu == 2:
        menu_header('NOVO CADASTRO')
        name = user_name('Nome: ')
        age = user_age('Idade: ')
        #abre os dados para ser cadastrados
    elif option_menu == 3:
        print('222')        
        #abre a opcao de escolher ver os dados complestos de algum usuario desde que digite o numero do mesmo
    elif option_menu == 4:
        print('fim')
        break
        #para o programa
    else:
        print('Digite somente uma das opções acima(1, 2, 3 ou 4)')