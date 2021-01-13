def anagrama(palabra1, palabra2):
    if len(palabra1) != len(palabra2): 
        print("no son anagramas") 
    for letra in palabra1 : 
        if(palabra2.index(letra)) :
            print("Si son anagramas")
        else:
            print("No son anagramas")


anagrama("caro", "roca")