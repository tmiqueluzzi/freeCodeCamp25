import random, string


senhas = int(input('Quantas chaves serão criadas? '))
tamanho = int(input('Quantos caracteres terão essas chaves? '))

for x in range(senhas):
    print(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(tamanho)))