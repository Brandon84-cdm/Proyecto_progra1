import os,json,calendar,datetime, locale

hashmap = [] #DICCIONARIO DONDE VAMOS A PONER LAS LISTAS
respuesta = "" 
while respuesta!=1:

    #INGRESO DEL TIPO DE VEHICULOS
    tipo_de_vehiculo = int(input("TIPO DE VEHICULO: "))
    while int(tipo_de_vehiculo)<1 or int(tipo_de_vehiculo)>3:
        print("SOLO HAY TRES TIPOS DE VEHICULO: 1 , 2 , 3")
        tipo_de_vehiculo = int(input("TIPO DE VEHICULO: "))
    
    #INGRESO DEL TIPO DE CLIENTE
    tipo_de_cliente = int(input("TIPO DE CLIENTE: "))
    while int(tipo_de_cliente)<1 or int(tipo_de_cliente)>2:
        print("SOLO HAY DOS TIPOS DE CLIENTE: 1 , 2")
        tipo_de_cliente = int(input("TIPO DE CLIENTE: "))

    #ESTO SIRVE PARA SABER EL DIA DE LA SEMANA
    x = datetime.datetime.now()
    dicdias = {'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves', \
    'FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo'}
    anho = x.year
    mes =  x.month
    dia= x.day
    fecha = datetime.date(anho, mes, dia)
    dia_de_la_semana = (dicdias[fecha.strftime('%A').upper()])

    precio = 0
    descuento = 0
    total = 0

    #COMPROVAMOS SI ES UN DIA ENTRE SEMANA
    if dia_de_la_semana != "sabado" and dia_de_la_semana != "domingo":
        
        #COMPROBACION DE VEHICULO MOTOCICLETA
        if int(tipo_de_vehiculo)==1:
            vehiculo="Motocicleta"
            precio=15
            if tipo_de_cliente==2:
                descuento = precio*0.20
            else:
                descuento=precio*0.10

        #COMPROBACION DE VEHICULO AUTOMOVIL
        if int(tipo_de_vehiculo)==2:
            vehiculo="Automovil"
            precio = 30
            if tipo_de_cliente==2:
                descuento=precio*0.20
            else:
                descuento = precio*0.10

        #COMPROBACION DE VEHICULO CAMIONETA
        if int(tipo_de_vehiculo)==3:
            vehiculo="Camioneta"
            precio = 50
            if int(tipo_de_cliente)==2:
                descuento=precio*0.20
            else:
                descuento=precio*0.10

        #COMPROVAMOS QUE TIPO DE CLIENTE TENEMOS
        if int(tipo_de_cliente)==2:
            cliente="Miembro"
        else:
            cliente="Estandar"

        #COMPROVAMOS QUE DIA DE LA SEMANA ES
        if dia_de_la_semana != "sabado" and dia_de_la_semana != "domingo":
            fin_de_semana="false"
        else:
            fin_de_semana="true"
        
        #OBTENEMOS EL TOTAL
        total=precio-descuento

        #OBTENEMOS LOS DATOS Y SE LO ASIGNAMOS A LA LISTA
        lista={}
        lista['Tipo']=vehiculo
        lista['Precio']=precio
        lista['Cliente']=cliente
        lista['Fin de semana']=fin_de_semana
        lista['Descuentos']=descuento
        lista['Total']=total

        #LLENAMOS EL HASHMAP CON LA LISTA
        hashmap.append(lista)
    

    #PREGUNTAMOS SI DESEAMOS ROMPER EL BUCLE            
    respuesta = int(input("PRECIONE 1 PARA SALIR, 2 PARA CONTINUAR: "))

#INGRESO DE EL NOMBRE DEL DOCUMENTO Y LA RUTA DE EXPORTACION
nombre_archivo=input("INGRESE NOMBRE DEL ARCHIVO: ")
ruta_exportacion=input("INGRESE LA RUTA DE EXPORTACION: ")

#EXPORTAMOS EL ARCHIVO
with open(str(ruta_exportacion)+nombre_archivo+'.json','w') as archivo:
    json.dump(hashmap, archivo)
    print("¡LISTA EXPORTADA EXITOSAMENTE!")
    print("_________________________________________________\n")
    print("CONTENIDO DE LA LISTA EXPORTADA: \n")
    
#LEEMOS EL ARCHIVO EXPORTADO ANTERIORMENTE
with open(str(ruta_exportacion)+nombre_archivo+'.json','r') as archivo:
    hashmap=json.load(archivo)
    print(hashmap)