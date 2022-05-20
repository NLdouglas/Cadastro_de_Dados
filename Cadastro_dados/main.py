from interface import* # FAZER PARTE DA INTERFACE

arquivo_cadastro = 'cadastros.txt'
if not arquivo_cadastro:
    criar_arquivo(arquivo_cadastro)

while True:
    opcao_menu = menu(['Fazer Cadastro', 'Fazer Login', 'Sair do programa'])
    if opcao_menu == 1:
        fazer_cadastro('Novo Cadastro')
        nome_cadastro = str(input('Nome para login: '))
        senha_cadastro = int(input('Digite sua senha: '))
        cadastrar_usuario(arquivo_cadastro, nome_cadastro, senha_cadastro)
    elif opcao_menu == 2:
        fazer_login('Login')
        nome_entrada = str(input('Nome: '))
        senha_entrada = int(input('Senha: '))
        continue
    while True:
        #PROGRAMA PARA CALCULAR % DE ACRESCIMO OU DESCONTO DE ALGUM VALO