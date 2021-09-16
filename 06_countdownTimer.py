import time

#definir processo
def cronometro(t):
    while t>=0:
        min, seg = divmod(t, 60) #dividir os segundos em min e seg
        timer = '{:02d}:{:02d}'.format(min, seg)
        print (timer)
        time.sleep(1)
        t -= 1

    print('DONE!')

#inserir o tempo
t = int(input('Quantos segundos o cronometro? '))

#play
cronometro(t)