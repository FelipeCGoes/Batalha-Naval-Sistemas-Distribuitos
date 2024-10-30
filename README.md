# Jogo Batalha naval - MATA88
Implementação do projeto de sistemas distribuídos (MATA88) da UFBA. Código implementado em Python. 

Como projeto final da disciplina de sistemas distribuídos da Universidade Federal da Bahia (UFBA), foi implementado um jogo de batalha naval através do terminal com jogadores em máquinas distintas, ou janelas distintas na execução local. O jogo consiste no formato clássico da Batalha naval tendo 4 tipos de navios em quantidades pré-definidas posicionados ao longo do tabuleiro 10x10 pelo jogador com cada jogador podendo dar um tiro por vez. O jogo termina quando um dos jogadores afundar todos os navios do inimigo ou ambos jogadores ultrapassarem o limite de tiros. O programa consiste de uma aplicação que implementa o cliente jogador e uma aplicação que implementa o servidor. A aplicação do cliente jogador implementa inserção auxiliada dos navios no tabuleiro, necessita apenas das duas primeiras coordenadas de posição do navio (definição da posição e da orientação) para posicioná-lo, e inclui tratamento de diversos casos de erro (posicionamento inicial do navio inválido, posicionamento inicial do navio já ocupado, repetição do tiro, input mal formatado). O servidor conecta clientes dois a dois para jogar, lida com toda a passagem de informação entre jogadores, mais especificamente, os tiros, os resultados desses tiros e o status do jogo, e alterna às vezes dos jogadores. 

No momento a versão funcional opera com clientes locais, porém pode ser adaptado para se conectar a um servidor remoto que troca mensagens entre clientes também remotos.

## Observações 
Execute o código na nova versão do WindowsPowerShell pois prevê impressão dos caracteres em cores e, se não for compativel com o terminal, a impressão do tabuleiro será feita de forma não legivel.

Impressão correta:

![image](https://github.com/FelipeCGoes/batalha-naval-MATA88/assets/64505429/7a7d0fd7-bff7-4e43-9f02-431eb9330e6e)

Impressão errada:

![image](https://github.com/FelipeCGoes/batalha-naval-MATA88/assets/64505429/ac54e9cb-5fa4-478b-85ff-b559617a5b1d)
