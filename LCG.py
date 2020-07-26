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

print (S4) 