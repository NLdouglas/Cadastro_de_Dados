perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2',
        'resposta': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'Pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6'},
        'resposta_certa': 'c',
    }
}

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["perguntas"]}')