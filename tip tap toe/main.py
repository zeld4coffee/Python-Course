import os
import random

jogarNovamente = 's'
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = 'n'
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def tela():
    global velha
    global jogadas
    os.system('cls')
    print('    0   1   2')
    print('0:  ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
    print('   -----------')
    print('1:  ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
    print('   -----------')
    print('2:  ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])
    print('Jogadas: ' + str(jogadas))


def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        l = int(input('Linha..: '))
        c = int(input('Coluna.: '))
        try:
            while velha[l][c] != " ":
                l = int(input('Linha..: '))
                c = int(input('Coluna.: '))
            velha[l][c] = 'X'
            quemJoga = 1
            jogadas += 1
        except:
            print('Jogada inválida')
            os.system('pause')
            # vit='n'

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = int(input('Linha..: '))
        c = int(input('Coluna.: '))
        while velha[l][c] != " ":
            l = int(input('Coluna.: '))
            c = int(input('Coluna.: '))
        velha[l][c] = 'O'
        jogadas += 1
        quemJoga = 2

def verificarvitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        # linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (velha[il][ic] == s):
                    soma += 1
                ic += 1
            if (soma == 3):
                vitoria = s
                break
            il += 1
        if (vitoria != "n"):
            break
        # colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il > 3:
                if (velha[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != "n"):
            break
        # diagonal1
        soma = 0
        idiag = 0
        while idiag < 3:
            if (velha[idiag][idiag] == s):
                soma += 1
            idiag += 1
        if (soma == 3):
            vitoria = s
            break
        # diagonal2
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if (velha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    vit = "n"
    velha = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

while (jogarNovamente == 's'):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit = verificarvitoria()
        if (vit != 'n') or (jogadas > maxJogadas):
            break

    print("Fim de jogo")
    if (vit == 'X' or vit == "O"):
        print("Resultado: Jogador " + vit + ' venceu ')
    else:
        print('Resultado: Empate')
    jogarNovamente = input('Jogar Novamente? [s/n]')
    redefinir()