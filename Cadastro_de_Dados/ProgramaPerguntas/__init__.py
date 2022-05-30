# FAZER TEXTO EXPLICATIVO NA INTERFACE OU EM UM MODULO SEPARADO
from time import sleep

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6',},
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items(): # pk = perguntas keys, pv = perguntas values
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha uma das opções abaixo: (Digite: A, B OU C)')
    for rk, rv in pv["respostas"].items():
        print(f'[{rk}]: {rv}')
    print()
    sleep(1)
    resposta_usuario = input('Digite a opção desejada(A, B ou C): ')
    for resp in resposta_usuario:
        if resposta_usuario != str:
            print('digite somente A, B ou C')

    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou!!')
        respostas_certas += 1
    else:
        print('Você errou!!')
    print()
    sleep(1.5)

qntd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qntd_perguntas * 100
print(f'Voce acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acertos foi de {porcentagem_acerto}')