from time import sleep

def linha(tam=60):
    print('~' * tam)


def cabecalho(msg):
    linha(60)
    print(f'\033[33m{msg}\033[m'.center(60))
    linha(60)


def menuOpc(msg):
    linha()
    print(f'\033[33m{msg}\033[m'.center(60))
    linha()
    opcoes = ['Som', 'Créditos', 'Voltar']
    c = 1
    for i in opcoes:
        print(f'{c} - {i}')
        c += 1
    linha()


def menuPrinc(msg):
    linha()
    print(f'\033[33m{msg}\033[m'.center(60))
    linha()
    opcoes = ['Começar', 'Opções', 'Sair']
    c=1
    for i in opcoes:
        print(f'{c} - {i}')
        c +=1
    linha()


# perguntas
def pergunta():
    perguntas = {
        'Pergunta1': {
            'pergunta': 'Qual a opção correta para declarar uma lista?',
            'respostas': {
                'a': 'lista = () e list:[]',
                'b': 'lista = [] e lista = list()',
                'c': 'list = lista() e lista: lista{}',
                'd': 'Nenhuma das acima',
            },
            'resposta_certa': 'b',
        },
        'Pergunta2': {
            'pergunta': 'Qual a diferença de uma Tupla pra uma Lista?',
            'respostas': {
                'a': 'Tuplas não podem conter listas',
                'b': 'Tuplas contém valores iteráveis',
                'c': 'Tuplas são imutáveis',
                'd': 'Listas podem guardar chaves nomeadas',
            },
            'resposta_certa': 'c',
        },
        'Pergunta3': {
            'pergunta': 'Qual destas palavras é uma palavra reservada em Python?',
            'respostas': {
                'a': 'copiar',
                'b': 'names',
                'c': 'restrict',
                'd': 'if',
            },
            'resposta_certa': 'd',
        },
        'Pergunta4': {
            'pergunta': 'Qual é a forma de dizer "tchau" ao Python no modo interativo?',
            'respostas': {
                'a': 'quit()',
                'b': 'while',
                'c': '#exit',
                'd': '//stop',
            },
            'resposta_certa': 'a',
        },
        'Pergunta5': {
            'pergunta': 'O quê é impresso na tela pelo programa abaixo?\n\nx = 5\nx = x + 10\nprint(x)',
            'respostas': {
                'a': '5',
                'b': 'print x',
                'c': 'x + 10',
                'd': '15',
            },
            'resposta_certa': 'd',
        },
        'Pergunta6': {
            'pergunta': '''No programa abaixo, o que será printado na tela?
    
lista = [2, 8, 4, 7]
lista.pop()
lista.insert(1,3)
lista.append(6)
print(lista)''',
            'respostas': {
                'a': '[1, 3, 2, 4, 6]',
                'b': '[2, 3, 8, 4, 6]',
                'c': '[2, 3, 8, 7, 6]',
                'd': '[1, 2, 3, 8, 4]',
            },
            'resposta_certa': 'b',
        },
        'Pergunta7': {
            'pergunta': '''O que é printado na tela?
 
vogais = ["a", "e", "i", "o", "u"]
print("As vogais são: ", end="")
for i in vogais:
    print(f"{i}", end=" ")''',
            'respostas': {
                'a': 'As vogais são: ["a", "e", "i", "o", "u"]',
                'b': 'As vogais são: a, e, i, o, u ',
                'c': 'As vogais são: a e i o u ',
                'd': '["a", "e", "i", "o", "u"]',
            },
            'resposta_certa': 'c',
        },
        'Pergunta8': {
            'pergunta': 'Alguma pergunta?',
            'respostas': {
                'a': 'copy',
                'b': 'names',
                'c': 'value',
                'd': 'if',
            },
            'resposta_certa': 'c',
        },
        'Pergunta9': {
            'pergunta': 'Outra pergunta?',
            'respostas': {
                'a': 'copy',
                'b': 'names',
                'c': 'value',
                'd': 'if',
            },
            'resposta_certa': 'c',
        },
        'Pergunta10': {
            'pergunta': 'Última pergunta?',
            'respostas': {
                'a': 'copy',
                'b': 'names',
                'c': 'value',
                'd': 'if',
            },
            'resposta_certa': 'c',
        }
    }
    vidas = 3
    pontos = 0
    respostas_certas = 0
    while True:
        for pk, pv in perguntas.items():
            if vidas == 0:
                print('\033[31mSinto muito. Você perdeu! Tente novamente.\033[m')
                break
            print(f'{pk}:\n{pv["pergunta"]}')
            print()
            print('Escolha uma resposta:')

            for rk, rv in pv['respostas'].items():
                print(f'[{rk}]: {rv}')

            # Verifica se é uma resposta válida
            while True:
                resposta_usuario = input('Resposta: ').lower()
                if resposta_usuario == 'a' or resposta_usuario == 'b' or resposta_usuario == 'c' or resposta_usuario == 'd':
                    break
                else:
                    print('\033[31mPrecisa escolher uma resposta válida.\033[m')

            # Verifica se a resposta está correta
            if resposta_usuario == pv['resposta_certa']:
                pontos += 100
                respostas_certas += 1
                print('Você acertou!')
                print(f'\033[33mVidas: {vidas}\t\t\t\t\t\tPontos: {pontos}\033[m')
                print()
            else:
                vidas -= 1
                print('\033[31mVocê errou. Perdeu uma vida.\033[m')
                print(f'\033[33mVidas: {vidas}\t\t\t\t\t\tPontos: {pontos}\033[m')
                print()

        # Faz a contagem final de pontos
        if respostas_certas == 10:
            print('\033[33mVocê é sensacional! Acertou Todas!!!\033[m'.center(60))
        print(f'\033[34mParabéns! Você venceu. Sua Pontuação foi de {pontos} Pontos.\033[m'.center(60))
        break
