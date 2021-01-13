def fizbuz():
    
    for numero in range(1,101):
        if numero % 3 == 0 :
            print('fizz')
        elif numero % 5 == 0:
            print('buzz')
        elif numero % 3 == 0 and numero % 5 == 0:
            print('fizbuz')
        else:
            print(numero)

fizbuz()

#La complejidad es 100