from time import sleep

def logo():
    print('''
                    \033[34m/////////////
                  //////////////*****
                  //    //////*******
                  //////////*********   \033[33m & & & & &
                  \033[34m(((((/////*********    \033[33m& & & & & & 
           \033[34m ///////////**************    \033[33m& & & & & & &
          \033[34m///////////****************    \033[33m& & & & & & & &
         \033[34m/////////*******************   \033[33m& & & & & & & & &
         \033[34m///////******************    \033[33m& & & & & & & & %%%
         \033[34m//////********   \033[33m& & & & & & & & & & & & & %%%%%
         \033[34m//////******   \033[33m& & & & & & & & & & & & & & %%%%
         \033[34m///*********   \033[33m& & & & & & & & & & & & & & %%%
          \033[34m//*********   \033[33m& & & & & & & & & & & & %%%%%
           \033[34m**********   \033[33m& & & & & & & & %%%%%%%%%%%
             \033[34m********   \033[33m& & & & & & & & & %%%
                        & & & & & & & & & %%%
                        & & & & &       & %%%
                        & & & %%%%%%%%%%%%%%
                            & & %%%%%%%%%%%%\033[m
    ''')
    sleep(4)
    

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo.')
    else:
        cabecalho('Pontuações dos Jogadores!')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<50}{dado[1]:>8}')
        sleep(3)
    finally:
        a.close()


def criar_relatorio(arq, nome, pontuacao):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{pontuacao}\n')
        except:
            print('Houve um ERRO ao escrever no arquivo.')
        else:
            print(f'Novo registro de {nome} adicionado.')


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
    opcoes = ['Jogar', 'Opções', 'Records', 'Sair']
    c=1
    for i in opcoes:
        print(f'{c} - {i}')
        c +=1
    linha()


def menuSom(msg):
    print('Menu de som')
    linha()
    print(f'\033[33m{msg}\033[m'.center(60))
    linha()
    opcoes = ['Mudo', 'Volume', 'Sair']
    c = 1
    for i in opcoes:
        print(f'{c} - {i}')
        c += 1
    linha()

def menuFinal(msg):
    linha()
    print(f'\033[33m{msg}\033[m'.center(60))
    linha()
    opcoes = ['Tentar Novamente', 'Records', 'Sair']
    c=1
    for i in opcoes:
        print(f'{c} - {i}')
        c +=1
    linha()
    sleep(0.5)
    opc = int(input('Sua opção: '))
    linha()
    if opc == 1:
        pergunta()
    elif opc == 2:
        ler_arquivo(relatorio)
        linha()



# perguntas
def pergunta():
    global relatorio
    perguntas_educ = {
        '\033[33mPergunta 1\033[m': {
            'pergunta': 'Qual a opção correta para declarar uma lista?',
            'respostas': {
                'a': 'lista = () e list:[]',
                'b': 'lista = [] e lista = list()',
                'c': 'list = lista() e lista: lista{}',
                'd': 'Nenhuma das questões acima',
            },
            'resposta_certa': 'b',
        },
        '\033[33mPergunta 2\033[m': {
            'pergunta': 'Qual a diferença de uma Tupla pra uma Lista?',
            'respostas': {
                'a': 'Tuplas não podem conter listas',
                'b': 'Tuplas contém valores iteráveis',
                'c': 'Tuplas são imutáveis',
                'd': 'Listas podem guardar chaves nomeadas',
            },
            'resposta_certa': 'c',
        },
        '\033[33mPergunta 3\033[m': {
            'pergunta': 'Qual destas palavras é uma palavra reservada em Python?',
            'respostas': {
                'a': 'copiar',
                'b': 'names',
                'c': 'restrict',
                'd': 'if',
            },
            'resposta_certa': 'd',
        },
        '\033[33mPergunta 4\033[m': {
            'pergunta': 'Qual é a forma de dizer "tchau" ao Python no modo interativo?',
            'respostas': {
                'a': 'quit()',
                'b': 'while',
                'c': '#exit',
                'd': '//stop',
            },
            'resposta_certa': 'a',
        },
        '\033[33mPergunta 5\033[m': {
            'pergunta': 'O quê é impresso na tela pelo programa abaixo?\n\nx = 5\nx = x + 10\nprint(x)',
            'respostas': {
                'a': '5',
                'b': 'print x',
                'c': 'x + 10',
                'd': '15',
            },
            'resposta_certa': 'd',
        },
        '\033[33mPergunta 6\033[m': {
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
        '\033[33mPergunta 7\033[m': {
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
        '\033[33mPergunta 8\033[m': {
            'pergunta': 'Para que serve a modularização?',
            'respostas': {
                'a': 'Organizar as funções, para que o programa fique mais legível',
                'b': 'Deixar o código bonitinho',
                'c': 'Diminuir o comondo',
                'd': 'Serve para habilitar o comando def',
            },
            'resposta_certa': 'a',
        },
        '\033[33mPergunta 9\033[m': {
            'pergunta': 'Qual deve ser a preferência para utilizar os laços For ou While?',
            'respostas': {
                'a': 'While é utilizado quando há um limite pre-definido',
                'b': 'O laço For é mais rapido que o While, por isso é preferivel usar o For',
                'c': 'For é utilizado quando há um limite pre-definido',
                'd': 'Nenhuma das questões acima',
            },
            'resposta_certa': 'c',
        },
        '\033[33mPergunta 10\033[m': {
            'pergunta': 'Qual o comando deve ser utilizado para importar a biblioteca math?',
            'respostas': {
                'a': 'a=(math.sqtr)',
                'b': 'from math import arithmetic',
                'c': 'import math',
                'd': 'from math import sqtr',
            },
            'resposta_certa': 'c',
        }
    }

    vidas = 3
    pontos = 0
    respostas_certas = 0

    while True:
        relatorio = 'relatorio.txt'
        # Loop de perguntas
        for pk, pv in perguntas_educ.items():
            if vidas == 0:
                print('\033[31mSinto muito. Você perdeu!\033[m')
                break
            print(f'{pk}:\n{pv["pergunta"]}')
            print()
            print('Escolha uma resposta:')
            
            # Loop de respostas
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
                if pontos == 0:
                    pontos += 100
                elif pontos > 0:
                    pontos += 100
                    pontos = (pontos + (pontos * 0.1))
                print('\033[34mVocê acertou!\033[m')
                print(f'\033[33mVidas: {vidas}\t\t\t\t\t\tPontos: {pontos}\033[m')
                print()
            else:
                vidas -= 1
                pontos = (pontos - (pontos * 0.1))
                print('\033[31mVocê errou. Perdeu uma vida.\033[m')
                print(f'\033[33mVidas: {vidas}\t\t\t\t\t\tPontos: {pontos}\033[m')
                print()

        # Faz a contagem final de pontos
        if respostas_certas == 10:
            print('\033[33mVocê é sensacional! Acertou Todas!!!\033[m'.center(60))
            print(f'\033[34mParabéns! Você venceu. \033[m'.center(60))
        linha()
        print(f'\033[34mSua Pontuação foi de {pontos} Pontos.\033[m'.center(60))
        linha()
        nome = input('Diga seu nome: ')
        criar_relatorio(relatorio, nome, pontos)
        menuFinal('Selecione uma opção')
        break

