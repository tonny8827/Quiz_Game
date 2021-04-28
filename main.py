from time import sleep
from interface.menus import *

pysolvers = ['\033[34mGabriel Correia (gothmate)',
             'Pablo Narciso',
             'Antonio (Tonny)',
             'Eduardo Gonçalves',
             'Ricardo Garcêz\033[m',
             ]

cabecalho('QUIZ PySolvers 2.0')
print('''\033[33mBem vindo ao Quiz Game.
Meu nome é Py15-A e vou te acompanhar nesse processo.
Você tem 3 chances! Não as desperdice.\033[m''')

while True:
    sleep(1)
    menuPrinc('ESCOLHA UMA OPÇÃO')
    sleep(1)
    opc = int(input('Escolha: '))
    if opc == 1:
        pergunta()
    elif opc == 2:
        while True:
            menuOpc('OPÇÕES')
            opc = int(input('Escolha uma opção: '))
            if opc == 1:
                print('Opção Som')
                sleep(3)
            elif opc == 2:
                cabecalho('EQUIPE PySolvers')
                for i in pysolvers:
                    print(f'{i}'.center(60))
                    sleep(3)
                sleep(3)
            else:
                break
    elif opc == 3:
        print('\033[31mSaindo do jogo. Até a próxima...\033[m')
        break
