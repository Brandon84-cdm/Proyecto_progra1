#proyecto realizado por grupo 14
#integrantes:
#Duglas Omar Subuyuc Rivera       - Carnet 1990 - 19 - 7812
#Josue Manuel Bocel Sequen        - Carnet 1990 - 18 - 4867
#Brandon Francisco Bartolomin Can - Carnet 1990 - 18 - 21016

from random import randint
from collections import deque

historial = deque()
numero = randint(1, 3)

print(f'Ingrese su opcion \n1) Piedra \n2) Papel \n3) Tijera')
respuesta = "1"
while respuesta == "1":
    eleccion = input("ingrese su opcion:\n")
    if int(eleccion) == 1 and int(numero) == 2:
        resultado="Computadora: Papel \n Humano: Piedra \n Resultado: ¡Gana Computadora!"
        historial.append(resultado)
        print (f'\n {resultado} \n')

    if int(eleccion) == 2 and int(numero) == 3:
        resultado="Computadora: Tijera \n Humano: Papel \n Resultado: ¡Gana Computadora!"
        historial.append(resultado)
        print (f'\n {resultado} \n')

    if int(eleccion) == 3 and int(numero) == 1:
        resultado="Computadora: Piedra \n Humano: Tijera \n Resultado: ¡Gana Computadora!"
        historial.append(resultado)
        print (f'\n {resultado} \n')

    if int(eleccion) == 2 and int(numero) == 1:
        resultado="Computadora: Piedra \n Humano: Papel \n Resultado: ¡Gana Humano!"
        historial.append(resultado)
        print (f'\n {resultado} \n')

    if int(eleccion) == 3 and int(numero) == 2:
        resultado="Computadora: Papel \n Humano: Tijera \n Resultado: ¡Gana Humano!"
        historial.append(resultado)
        print (f'\n {resultado} \n')

    if int(eleccion) == 1 and int(numero) == 3:
        resultado="Computadora: Tijera \n Humano: Piedra \n Resultado: ¡Gana Humano!"
        historial.append(resultado)
        print (f'\n {resultado} \n')

    if int(eleccion) == 1 and int(numero) == 1:
        resultado="Computadora: Piedra \n Humano: Piedra \n Resultado: ¡Empate!"
        historial.append(resultado)
        print (f'\n {resultado} \n')

    if int(eleccion) == 2 and int(numero) == 2:
        resultado="Computadora: Papel \n Humano: Papel \n Resultado: ¡Empate!"
        historial.append(resultado)
        print (f'\n {resultado} \n')

    if int(eleccion) == 3 and int(numero) == 3:
        resultado="Computadora: Tijera \n Humano: Tijera \n Resultado: ¡Empate!"
        historial.append(resultado)
        print (f'\n {resultado} \n')
    
    

    historial.append(eleccion)
    print(f'1) jugar otra vez \n2) ver resultado anterior \n3) salir')
    respuesta=input()
    
    if respuesta == "1":
        numero= randint(1, 3)
        print(f'Ingrese su opcion \n1) Piedra \n2) Papel \n3) Tijera')
    if respuesta == "2":
        while len(historial) > 0:
            acction = historial.pop()
            print(f'{acction} \n')
        print(f'1) jugar otra vez \n2) ver resultado anterior \n3) salir')
        respuesta=input()
        

    

    