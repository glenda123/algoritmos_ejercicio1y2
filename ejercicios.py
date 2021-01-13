

def puntuacion_palabras(array_de_palabras):
    
    puntuacion_final = 0    #1
    for palabra in array_de_palabras:  #n
        count = 0 #1
        for letra in palabra: #10
            if letra.lower() in ['a','e','i','o','u']: #1
                count = count + 1 #1
        if count % 2 == 0: #1
            puntuacion_final = puntuacion_final + 2 #1
        else: #1
            puntuacion_final = puntuacion_final + 1 #1
            
    return puntuacion_final #1

# 1+n*(1+10+1+1+1+1+1+1) + 1 = 1+ 25n + 1 = 2 + 25n = n

puntuacion_palabras(['amigos y estudiantes', 'programadores imparables', 'agradecidos con Dios'])