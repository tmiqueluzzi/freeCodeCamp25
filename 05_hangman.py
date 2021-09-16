from random import choice

lista = ['livro', 'caneta', 'garfo','panela','mesa','cama','microfone', 'celular','martelo','bolsa','criança','menina']
palavra = choice(lista).upper()

letras_erradas = []
letras_certas = []
acertos = erros = 0



while True:
    acertos = 0
    for letra in palavra:
        if letra not in letras_certas:
            print('_', end = ' ')

        else:
            print(letra, end = ' ')
            acertos += 1

    if acertos == len(palavra):
        print(' - VOCÊ VENCEU. PARABÉNS!')
        break


    print(f'\nAté agora você errou {erros} vez(es). As letras erradas são: {letras_erradas}')
    print(f'Até agora, faltam {len(palavra) - acertos} letras.')
    jogador = input('Digite uma letra: ').upper()

    if jogador in palavra:
        letras_certas.append(jogador)
    else:
        erros += 1
        letras_erradas.append(jogador)
    if erros == 6:
        print(f'SEIS ERROS. VOCÊ PERDEU. A PALAVRA ERA {palavra}. TENTE NOVAMENTE')
        break
