#Random module for randomly accepting the values
# ‘X’ indicates the ships hit
# ‘-‘ indicates the hits missed
from random import randint
import socket

global tabuleiroA
tabuleiroA = []
for i in range(10):
    tabuleiroA.append(['0']*10)

global tabuleiroB
tabuleiroB = []
for i in range(10):
    tabuleiroB.append(['0']*10)

#posicoes_lcima = [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [1,9], [1,10]]
#posicoes_lesquerda = [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [1,9], [1,10]]
#posicoes_ldireita = [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [1,9], [1,10]]
#posicoes_lbaixo = [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [1,9], [1,10]]

def input_linha_valida():
    linha = input("Insira uma linha 1-10: ")
    while linha not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print("Insira um valor valido [1-10]")
        linha = input()
    return int(linha)-1 #deixar no formato 0-9

def input_coluna_valida():
    coluna = input("Insira uma coluna 1-10: ")
    while coluna not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print("Insira um valor valido [1-10]")
        coluna = input()
    return int(coluna)-1 #deixar no formato 0-9

colors = {
    "reset":"\033[00m",
    "red":"\033[91m",
    "blue":"\033[94m",
    "cyan":"\033[96m",
}

def print_board(tabuleiro):
    print('  1 2 3 4 5 6 7 8 9 10')
    cont = 1
    for i in range(10):
        print(f"{i+1} ", end="")
        print(colors['blue'], end="")
        for item in tabuleiro[i]:
            if item == '-1':
                print(colors['red'], end="")
                print("X ", end="")
                print(colors['blue'], end="")
            elif item == '1':
                print(colors['cyan'], end="")
                print("- ", end="")
                print(colors['blue'], end="")
            elif item != '0':
                print(colors['reset'], end="")
                print(f"{item} ", end="")
                print(colors['blue'], end="")
            else:
                print(f"{item} ", end="")
        print(colors['reset'])

def print_2_tabuleiros(tabuleiroA, tabuleiroB):
    print('  1 2 3 4 5 6 7 8 9 10    |       1 2 3 4 5 6 7 8 9 10')
    cont = 1
    for i in range(10):
        print(f"{i+1} ", end="")
        print(colors['blue'], end="")
        for item in tabuleiroA[i]:
            if item == '-1':
                print(colors['red'], end="")
                print("X ", end="")
                print(colors['blue'], end="")
            elif item == '1':
                print(colors['cyan'], end="")
                print("- ", end="")
                print(colors['blue'], end="")
            elif item != '0':
                print(colors['reset'], end="")
                print(f"{item} ", end="")
                print(colors['blue'], end="")
            else:
                print(f"{item} ", end="")
        print(colors['reset'], end="")
        if i==9:
            print(f"   |     {i+1} ", end="")
        else:
            print(f"    |     {i+1} ", end="")
        print(colors['blue'], end="")
        for item in tabuleiroB[i]:
            if item == '-1':
                print(colors['red'], end="")
                print("X ", end="")
                print(colors['blue'], end="")
            elif item == '1':
                print(colors['cyan'], end="")
                print("- ", end="")
                print(colors['blue'], end="")
            elif item != '0':
                print(colors['reset'], end="")
                print(f"{item} ", end="")
                print(colors['blue'], end="")
            else:
                print(f"{item} ", end="")
        print(colors['reset'])
    print("     Minha frota          |          Frota inimiga     ")

#Function that creates the ships
def create_ships(tabuleiro):
    print("Voce ira posicionar os seus navios estrategicamente no campo de batalha")
    for i in range(5):
        if i == 0:
            navio = "PORTA AVIOES"
            call_sign = 'P'
            tamanho_navio = 5
        elif i == 1:
            navio = "NAVIO DE GUERRA"
            call_sign = 'G'
            tamanho_navio = 4
        elif i == 2 or i == 3:
            navio = "CRUZADOR"
            call_sign = 'C'
            tamanho_navio = 3
        elif i == 4:
            navio = "SUBMARINO"
            call_sign = 'S'
            tamanho_navio = 2
        
        while True: #Repete ate que a inserção do navio seja bem sucedida
            coordenada = [0,0]
            posicao_navio = []

            print(f"{navio} - indique posicoes consecutivas na horizontal ou vertical | TAMANHO: {tamanho_navio}")

            #PRIMEIRA POSIÇÃO
            while True:
                coordenada[0] = input_linha_valida()
                coordenada[1] = input_coluna_valida()
                posicoes_possiveis = []

                if coordenada[0]-1>=0:
                    if tabuleiro[coordenada[0]-1][coordenada[1]] == '0':
                        posicoes_possiveis.append([coordenada[0]-1, coordenada[1]])

                if coordenada[0]+1<10:
                    if tabuleiro[coordenada[0]+1][coordenada[1]] == '0':
                        posicoes_possiveis.append([coordenada[0]+1, coordenada[1]])

                if coordenada[1]-1>=0:
                    if tabuleiro[coordenada[0]][coordenada[1]-1] == '0':
                         posicoes_possiveis.append([coordenada[0], coordenada[1]-1])

                if coordenada[1]+1<10:
                    if tabuleiro[coordenada[0]-1][coordenada[1]+1] == '0':
                        posicoes_possiveis.append([coordenada[0], coordenada[1]+1])
                #Verifica quais proximas possíveis apartir daquela posição e se ela está vazia. Com isso podemos verificar se existe proxima posição consecutiva disponível

                if tabuleiro[coordenada[0]][coordenada[1]] == "0" and not posicoes_possiveis: #verifica se a posição está livre e existe proxima posição consecutiva disponível
                    print("Nao ha posicoes sufucientes para posicionar navio partindo da posicao indicada")
                    print(f"{navio} - indique posicoes consecutivas na horizontal ou vertical | TAMANHO: {tamanho_navio}")
                elif tabuleiro[coordenada[0]][coordenada[1]] == '0':
                    posicao_navio.append(coordenada.copy())
                    break
                else:
                    print("Posicao ja ocupada por outro navio")
            #Com essa condição garantimos que a primeira posição escolhida está vazia
        
            #SEGUNDA POSIÇÃO
            while True:
                horizontal = False
                vertical = False
                sentido_positivo = False
                sentido_negativo = False
                salv_coordenada = coordenada.copy()

                while True:
                    linha = input_linha_valida()
                    if linha == coordenada[0]:
                        coordenada[0] = linha
                        horizontal = True
                        break
                    elif linha == coordenada[0] + 1:
                        coordenada[0] = linha
                        vertical = True
                        sentido_positivo = True
                        break 
                    elif linha == coordenada[0] - 1:
                        coordenada[0] = linha
                        vertical = True
                        sentido_negativo = True
                        break
                    else:
                        print("Insira uma linha valida, posicao final nao sera consecutiva")
                    
                while True: 
                    coluna = input_coluna_valida()   
                    if horizontal:
                        if coluna == coordenada[1] + 1:
                            coordenada[1] = coluna
                            sentido_positivo = True
                            break
                        elif coluna == coordenada[1] -1:
                            coordenada[1] = coluna
                            sentido_negativo = True
                            break
                        else:
                            print("Insira uma coluna valida, posicao final nao e consecutiva")
                    elif vertical:
                        if coluna == coordenada[1]:
                            coordenada[1] = coluna
                            break
                        else:
                            print("Insira uma coluna valida, posicao final nao e consecutiva")

                if tabuleiro[coordenada[0]][coordenada[1]] == '0':
                    posicao_navio.append(coordenada.copy())
                    break
                else:
                    print("Posicao ja ocupada por outro navio")
                    coordenada = salv_coordenada.copy()

            #PROXIMAS POSICOES
            #Definido o sentido, as proximas escolhas são fixas, não faz sentido deixar em aberto para o usuário escolher
            ocupado = False
            for i in range(tamanho_navio-2):    
                if horizontal:
                    if sentido_positivo:
                        coordenada[1] = coordenada[1] + 1
                    elif sentido_negativo:
                        coordenada[1] = coordenada[1] - 1
                    #coordenada[0] (linha) é fixa pois o sentido é horizontal
                elif vertical:
                    if sentido_positivo:
                        coordenada[0] = coordenada[0] + 1
                    elif sentido_negativo:
                        coordenada[0] = coordenada[0] - 1
                    #coordenada[1] (coluna) é fixa pois o sentido é vertical
        
                if tabuleiro[coordenada[0]][coordenada[1]] == '0':
                    posicao_navio.append(coordenada.copy())
                else:
                    ocupado = True
                    #coordenada[1] (coluna) é fixa pois o sentido é vertical
                
                #A delimitação ocupado permite indicar se as demais posições estão livres ou não. Essa cobertura aliada à cobertura implementada acima sobre a segunda posição garante que sempre há espaço para inserir o navio
            if not ocupado:
                if horizontal:
                    print("Sentido do navio: HORIZONTAL")
                else:
                    print("Sentido do navio: VERTICAL")
                
                print("Demais posicoes preenchidas automaticamente a partir do sentido dado, navio inserido com suceso")
                for i in posicao_navio:
                    tabuleiro[i[0]][i[1]] = call_sign #Aplica as alterações ao tabuleiro 
                print_board(tabuleiro) 
                break
            else:
                print("Nao ha posicoes sufucientes para posicionar navio partindo da posicao indicada")    

global perdas_navios
perdas_navios = 0

def dar_tiro(vetor_tiros):
    tiro = [0, 0]
    print("Selecione a posicao que deseja atingir")
    while True:
        tiro[0] = input_linha_valida()
        tiro[1] = input_coluna_valida()
        if tiro not in vetor_tiros:
            vetor_tiros.append(tiro.copy())
            return tiro[0], tiro[1]
        else:
            print("Tiro ja dado anteriormente, selecione outra posicao")

def verificarTiro(linha, coluna):
    if tabuleiroA[linha][coluna] in "PGCS":
        global perdas_navios
        perdas_navios = perdas_navios + 1
        tabuleiroA[linha][coluna] = "-1"
        print_2_tabuleiros(tabuleiroA, tabuleiroB)
        print("O adversario acertou um tiro na sua frota!")
        return 1
    else:
        tabuleiroA[linha][coluna] = "1"
        print_2_tabuleiros(tabuleiroA, tabuleiroB)
        print("O adversario errou o tiro!")
        return 0

def attTiroDado(linha, coluna, result, acertos):
    if result:
        acertos += 1
        tabuleiroB[linha][coluna] = "-1"
        print_2_tabuleiros(tabuleiroA, tabuleiroB)
        print("Parabens Jogador! Voce acertou um tiro na frota inimiga")
    else:
        tabuleiroB[linha][coluna] = "1"
        print_2_tabuleiros(tabuleiroA, tabuleiroB)
        print("Voce errou o tiro")


print("--------BATALHA NAVAL--------")
print("Bem vindo Jogador!")
create_ships(tabuleiroA)

#Auxiliares
vetor_tiros = []
total_de_tiros = 5
acertos = 0
message = [0,0,0,0,0,0]
dataRecv = [0,0,0,0,0,0]

#Conectar co servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 40000))
print("Conectado ao servidor")
print("Aguardando canexao do outro jogador")

dataRecv = s.recv(6)
dataRecv = list(dataRecv) #converte de volta de byte para lista

if dataRecv[5] == 1:
    print("Você esta liberado para dar o primeiro tiro")

    message[0], message[1] = dar_tiro(vetor_tiros)
    total_de_tiros -= 1
    s.send(bytes(message))
else:
    print("O adversario dara o primeiro tiro, aguarde")

    dataRecv = s.recv(6)
    dataRecv = list(dataRecv)
    
    message[2] = verificarTiro(dataRecv[0], dataRecv[1])
    message[0], message[1] = dar_tiro(vetor_tiros)
    total_de_tiros -= 1
    s.send(bytes(message))

while total_de_tiros>0:
    message = [0,0,0,0,0,0]
    
    print("Inimigo escolhendo posicao de tiro...")
    dataRecv = s.recv(6)
    dataRecv = list(dataRecv)

    attTiroDado(vetor_tiros[len(vetor_tiros)-1][0], vetor_tiros[len(vetor_tiros)-1][1], dataRecv[2], acertos)

    if dataRecv[3] == 1:
        print("Fim do jogo -- Voce saiu vitorioso da batalha!") 
        break
    else:
        message[2] = verificarTiro(dataRecv[0], dataRecv[1])

        if perdas_navios == 17:
            print("Você perdeu, o inimigo destruiu todos os seus navios")
            message[3] = 1
            s.send(bytes(message))
            break
        else:
            message[0], message[1] = dar_tiro(vetor_tiros)
            total_de_tiros -= 1
            s.send(bytes(message))

if total_de_tiros == 0:
    message = [0,0,0,0,0,0]

    print("Aguardando o tiro final do adversario...")
    dataRecv = s.recv(6)
    dataRecv = list(dataRecv)

    attTiroDado(vetor_tiros[len(vetor_tiros)-1][0], vetor_tiros[len(vetor_tiros)-1][1], dataRecv[2], acertos)

    if dataRecv[3] == 1:
        print("Fim do jogo -- Voce saiu vitorioso da batalha!")
    elif dataRecv[4] == 1:
        print("EMPATE, nenhuma das duas frotas foi destruida por completo")
    else:
        message[2] = verificarTiro(dataRecv[0], dataRecv[1])
        if perdas_navios == 17:
            message[3] = 1
            print("Você perdeu, o inimigo destruiu todos os seus navios") 
            s.send(bytes(message))
        else:   
            message[4] = 1
            print("EMPATE, nenhuma das duas frotas foi destruida por completo")
            s.send(bytes(message))