Num_Seed = int(input("Ingresa un numero de dos digitos: "))
numero = Num_Seed


for i in range (2):
    
    inicial = numero * numero 
    print ("valor inicial (cuadrado del valor dado):",inicial,"\n")

    print ("Verificamos si el numero es de 3 o 4 digitos\n")
    print ("Si el numero es de 3 digitos rellenamos con un 0")
    print ("con el fin de tener 4 digitos\n")
    num_in_text = str(inicial)
    print ("El tamaño del numero actual es de: ",len(num_in_text), "\n")
    
    num_in_text = num_in_text.zfill(4)
    print ("El numero ahora es ", num_in_text, "\n")
    new = num_in_text[1:-1]
    print ("El numero a elevar (tomando solo los dos digitos de en medio) ", new, "\n")
    numero = int(new)
    print ("<--y repetimos -->","\n")



