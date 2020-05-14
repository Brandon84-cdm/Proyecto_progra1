#proyecto realizado por grupo 14
#integrantes:
#Duglas Omar Subuyuc Rivera       - Carnet 1990 - 19 - 7812
#Josue Manuel Bocel Sequen        - Carnet 1990 - 18 - 4867
#Brandon Francisco Bartolomin Can - Carnet 1990 - 18 - 21016
from collections import deque
cola = deque()
ciclo = "y"
archivos=["Archivo1.txt","Archivo2.txt"]

def primer_eleccion():
    print(f'Ingrese el número de archivo que desea agregar a la cola:\n\n[1] Archivo1.txt \n[2] Archivo2.txt \n[0] Cancelar')
    accion_interna=input()
    if accion_interna == "1":
        cola.append(archivos[0])
    if accion_interna == "2":
        cola.append(archivos[1])
    print(f'\nLa cola de impresion es:\n{cola}\n')

def segunda_eleccion():
    print("\n")
    while len(cola) > 0:
        siguiente_elemento = cola.popleft()
        print(f'Se imprimio el archivo: {siguiente_elemento}')
        if len(cola)==0:
            print("Cola vacia")
        else:
            print(f'Cola de impresion: {cola}\n')
            

while ciclo == "y":
    print(f'[1] Agregar elemento a la cola de impresión \n[2] Imprimir \n[0] Salir')
    accion=input()
    if accion=="1":
        primer_eleccion()
    if accion=="2":
        segunda_eleccion()
    if accion=="0":
        ciclo = "n"

