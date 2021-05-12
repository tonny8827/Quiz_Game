from time import sleep
from interface.menus import logo, arquivo_existe, criar_arquivo, cabecalho, menuOpc, \
    linha, ler_arquivo, menuSom, menuPrinc, pergunta
import pygame
from pygame import mixer


pygame.init()
mixer.music.load('game.mp3')
mixer.music.play(-1)
mixer.music.set_volume(1.0)

pysolvers = ['\033[34mGabriel Correia (gothmate)',
             'Pablo Narciso',
             'Antonio (Tonny)',
             'Eduardo Gonçalves',
             'Ricardo Garcêz\033[m',
             ]

relatorio = 'relatorio.txt'
if not arquivo_existe(relatorio):
    criar_arquivo(relatorio)

logo()
cabecalho('QUIZ PySolvers 2.0')
print('''\033[33mBem vindo ao Quiz Game.
Meu nome é Py15-A e vou te acompanhar nesse processo.
Você tem 3 chances! Não as desperdice.\033[m''')

while True:
    # Menu Tela Inicial
    sleep(1)
    menuPrinc('ESCOLHA UMA OPÇÃO')
    sleep(1)
    try:
        opc = int(input('Escolha: '))
        if opc == 1:
            pergunta()
            print()
        elif opc == 2:
            while True:
                menuOpc('OPÇÕES')
                opc = int(input('Escolha uma opção: '))
                if opc == 1: #Menu de som
                    menuSom('OPÇÕES DE AUDIO')
                    sleep(1)
                    opca = int(input('Escolha uma opção: '))
                    if opca == 1:
                        mixer.music.set_volume(0)
                    elif opca == 2:
                        vol = float(input('Escolha o volume de 0[Min] a 10[Max]: '))/10
                        mixer.music.set_volume(vol)
                    else:
                        break
                elif opc == 2:
                    cabecalho('EQUIPE PySolvers')
                    for i in pysolvers:
                        print(f'{i}'.center(60))
                        sleep(3)
                    sleep(3)
                else:
                    break
        elif opc == 3:
            ler_arquivo(relatorio)
            linha()

        elif opc == 4:
            print('\033[31mSaindo do jogo. Até a próxima...\033[m')
            break
    except:
        print('\033[31mEssa não é uma opção válida. Tente novamente.\033[m')
