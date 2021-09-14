from random import randint
import time

#Variaveis
contagem = 0
limite_alto = 100
limite_baixo = 0

#Ambientação
print('~'*40)
print('JOGO DA ADIVINHAÇÃO PELO COMPUTADOR')
print('~'*40)

#Código
usuario = int(input('Digite um número de 1 a 100 para testar a sorte do seu processador: '))
if 0 > usuario  or usuario > 100:
    usuario = int(input('Número inválido. Selecione entre 1 e 100! '))

time.sleep(0.5)
print('Ok, agora vou pensar em um número.')
computador = randint(1, 100)
contagem += 1
while computador != usuario:
    if computador > usuario:
        time.sleep(0.5)
        print(f'{computador} é muito alto? Ok. Vou tentar de novo.')
        limite_alto = computador
    elif computador < usuario:
        time.sleep(0.5)
        print(f'{computador} é muito baixo? Ok. Vou tentar de novo')
        limite_baixo = computador
    computador = randint(limite_baixo, limite_alto)
    contagem += 1

print(f'Consegui na minha {contagem}a tentativa! Seu número era {usuario}')
