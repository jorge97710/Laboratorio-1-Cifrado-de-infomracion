'''
    Laboratorio No.1 
    PARTE 2: Linear Congruential Generator
    Grupo #1: Jorge Azmitia, Cristina Bautista, Abril Palencia, Sebastián Maldonado y César Rodas
    26/07/2020
'''
# Ejercicio No.1 
S3 = 2148910388216139
Multiplicador = 915451635481687
Incremento = 5886893188886454
Modulo = 6108133789056532
Cantidad_estados = 4
S4 = (S3 * Multiplicador + Incremento) % Modulo
print("Ejercicio No.1")
print("b. S4 =", S4) 

#Ejercicio No.2
s2 = 1251340539300040
s1 = 1526203935246140
modulo = 3059121001727213
multiplicador = 7544713835650436
incremento = (s2 - ((multiplicador * s1) % modulo)) + modulo
print("Ejercicio No.2")
print("b. incremento =", incremento) 
S3 = (s2 * multiplicador + incremento) % modulo
print("c. S3 =", S3) 
