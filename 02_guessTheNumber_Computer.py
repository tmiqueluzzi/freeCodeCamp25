from random import randint

#Variaveis
aleatorio = randint(1, 100) #Computador escolhe um numero
contador = 0 #contagem das tentativas

print('-='*20)
print('JOGO DA ADIVINHAÇÃO (com dicas)')
print('-='*20,'\n')
#Input escolha do usuario
usuario = int(input('Tente adivinhar o número sorteado entre 1 e 100! '))
while True:
    if 0 < usuario < 100:
        contador += 1
        if usuario == aleatorio:
            print(f'Parabéns! Você acertou na {contador}a tentativa.')
            break
        elif usuario < aleatorio:
            print('Seu número está muito baixo, tente algum mais alto.')
        else:
            print('Seu número está muito alto, tente algum mais baixo.')
    else:
        print('Número inválido. Insira um valor entre 1 e 100.')
    usuario = int(input('Próxima tentativa: '))
#Mais pra cima ou mais pra baixo?


#