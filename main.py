'''
Projeto Jogo Pedra-Papel-Tesoura
2024.08.13
Matheus Felix Mendes
'''

# --> Bibliotecas
# Importa funções do arquivo modules.py
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption
from ppt import startPPT
from parimpar import startParImpar

# --> Constantes, Variáveis e Listas

# --> Funções

# --> Main
# print('Teste 123')
# clrScreen() 
# displayLine()
# displayMsg('Esse é um teste de MSG')
# displayMsgCenter('Teste de mensgaem Centralizada')
# listaMsgs = ['oi', 'Esse é um', 'teste', 'do cabeçalho']
# displayHeader(listaMsgs) 
# msg = getUserOption('Digite algo')
# displayMsg(msg)

# escolha = getUserOption('Escolha [1, 2 ou 3]')
# listaValida = ['1', '2', '3'] # 1 != '1'
# while not validateUserOption(escolha, listaValida): 
  #escolha = getUserOption('Escolha [1, 2 ou 3]')
# displayMsg('ESCOLHA VÁLIDA')

msgs = ['Seja bem-vind@ aos Jogos', '', 'PAR OU ÍMPAR']
displayHeader(msgs)
msgs = ['Digite 0 --> Sair',
       'Digite 1 --> Pedra-Papel-Tesoura',
       'Digite 2 --> Par ou Ímpar']
displayHeaderT(msgs)
opUser = getUserOption('Sua escolha')
while not validateUserOption (opUser, ['0', '1', '2']):
  opUser = getUserOption('Sua escolha')
if(opUser == '1'):
  startPPT()
elif(opUser == '2'):
  starParImpar()
else:
  displayMsg('Até a Próxima...')
  
