import socket

SERVER = '127.0.0.1'
PORT = 40000

#Criação do socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER, PORT))

s.listen(2)
print("Servidor está aguardando conexões dos clientes")
conexaoJogadorA, endJogadorA = s.accept()
print(f"Conectado com cliente {endJogadorA}")
conexaoJogadorB, endJogadorB = s.accept()
print(f"Conectado com cliente {endJogadorB}")

#INICIALIZACAO DO JOGO
message = [0,0,0,0,0,1] #Pode enviar um tiro
conexaoJogadorA.send(bytes(message))

message = [0,0,0,0,0,0] #Aguarde
conexaoJogadorB.send(bytes(message))

#TROCA DE TIROS
data = [0,0,0,0,0,0]
while data[3] == 0 and data[4] == 0: #data[3] = 1 qundo alguem ganha data[4] = 1 quando empata e não precisa mais trocar mensagem
    data = conexaoJogadorA.recv(6)
    conexaoJogadorB.send(data)
    data = list(data)

    if data[3] != 0 or data[4] != 0: #se o jogador A anuncia ao B a vitória
        break

    data = conexaoJogadorB.recv(6)
    conexaoJogadorA.send(data)
    data = list(data)

print("Jogo finalizado, encerrando conexões")
conexaoJogadorA.close()
conexaoJogadorB.close()


