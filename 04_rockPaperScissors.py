import random

#Ambientação
print('~'*40)
print('PEDRA, PAPEL OU TESOURA?')
print('~'*40)

#Código
computador = random.randint(0 , 2)
usuario = int(input('Pedra [0] papel [1] ou tesoura [2]? '))
if 0> usuario or usuario > 2:
    usuario = int(input('Escolha inválida. Insira pedra [0] papel [1] ou tesoura [2]: '))

if usuario == computador:
    print('Jogo empatado!')
elif (usuario == 0 and computador == 1) or (usuario ==1 and computador == 2) or (usuario == 2 and computador ==0):
    print('Vitória do computador!')
else:
    print('Vitória do usuário! Parabéns!')