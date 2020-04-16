import os,json

nombres_actuales = [] #nombres de los archivos actualmente
correlativo = [] # guardamos el numero correlativo para cada archivo
nombres_nuevos = [] # guardamos el nuevo nombre que se le dara a cada archivo
hashmap = [] #aqui se guarda la lista de los antiguos y nuevos nombres para su posterior exportacion


#ESTO SIRVE PARA INGRESAR DATOS COMO LA RUTA, EL NOMBRE Y LA EXTENSION DE LOS ARCHIVOS Y LA RUTA DE EXPORTACION DEL JSON
ruta_archivos = input("RUTA DE LOS ARCHIVOS: ")
extension = input("INGRESE LA EXTENSION: ")
nuevo_nombre = input("INGRESE EL NOMBRE: ")
ruta_exportacion = input("¿DONDE DESEA EXPORTAR EL DOCUMENTO?: ")

#SIRVE PARA OBTENER LOS NOMBRES DE LOS ARCHIVOS QUE VIENEN DE LA CARPETA SELECCIONADA
for item in os.listdir(str(ruta_archivos)):
    nombres_actuales.append(item)

#SIRVE PARA ENUMERAR LOS ARCHIVOS QUE VIENEN EN LA RUTA
for index,i in enumerate(range(0,len(nombres_actuales))):
    #ESTE ES EL CORRELATIVO DE LOS ARCHIVOS
    correlativo.append(i)
    if nombres_actuales[index][-4:] == extension: #SIRVE PARA FILTRAR LOS ARCHIVOS POR MEDIO DE LA EXTENSION
        nombres_nuevos.append(nuevo_nombre + "_" + str(correlativo[index]) + extension) #ASIGNA UN NOMBRE Y CORRELATIVO A LOS ARCHIVOS
    os.rename((str(ruta_archivos)+nombres_actuales[index]), (str(ruta_archivos)+nombres_nuevos[index])) #CAMBIA LOS NOMBRES ANTIGUOS POR LOS NUEVOS

    #AQUI LLENAMOS LA LISTA CON LOS DATOS OBTENIDOS
    lista={}
    lista['Original']=nombres_actuales[index]
    lista['Nuevo']=nombres_nuevos[index]
    #LLENAMOS LA VARIABLE HASHMAP CON LAS LISTAS
    hashmap.append(lista)
    

#EXPORTAMOS EL DOCUMENTO EN UNA RUTA ESPECIFICA
with open(str(ruta_exportacion)+'documento.json','w') as archivo:
    json.dump(hashmap, archivo)
    print("¡LISTA EXPORTADA EXITOSAMENTE!")
    print("_________________________________________________\n")
    print("CONTENIDO DE LA LISTA EXPORTADA: \n")

#LEEMOS EL DOCUENTO QUE EXPORTAMOS ANTERIORMENTE
with open(str(ruta_exportacion)+'documento.json','r') as archivo:
    hashmap=json.load(archivo)
    print(hashmap)
