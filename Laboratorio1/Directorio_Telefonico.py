# Taller 1 Sistemas Digitales III

Mensajes = [#lista para textos a mostrar en pantalla
    "\n\n\tBienvenido al gestor del directorio telefonico",#0
    "Digite su nombre y apellido: ",#1
    "Digite su telefono celular: ",#2
    "Digite su fecha de cumpleaños dd/mm: ",#3
    "Digite su correo electronico: ",#4
    "\n\tGracias vuelva pronto\n",#5
    "\n\t*****Digite una opcion*****\n1.Agregar una nueva persona\n2.Borrar datos de una persona por numero de celular\n3.Buscar datos por numero de celular\n4.Cerrar directorio telefonico\n\t",
    "\n\tPersona agregada exitosamente",#7
    "Digite el numero de celular que desea borrar: ",#8
    "\n\tDatos eliminados exitosamente",#9
    "Numero de celular no encontrado, vuelva a digitar",#10
    "Digite el numero de celular que desea buscar: ",#11
    "\n\tDatos encontrados exitosamente",#12
    "\n\tOpcion no valida"#13
]

#lista para la informacion de las personas
Directorio = []

def Agregar_Persona():#Funcion para agregar nueva persona
    #Diccionario para los datos de la persona
    Persona = {
        "Nombre": input(Mensajes[1]),
        "Telefono": int(input(Mensajes[2])),
        "Cumpleaños": input(Mensajes[3]),
        "Correo": input(Mensajes[4])
    }

    Directorio.append(Persona)#Agregamos la persona a la lista del directorio
    print(Mensajes[7])

def Borrar_Persona():#Funcion para borrar persona
    bucle = 1#Inicializamos variable para crear un bucle
    while bucle == 1:#Creamos bucle en caso de no encontrar el numero
        telefono = int(input(Mensajes[8]))#Guardamos el numero que digito el usuario
        for i in range(len(Directorio)):#Recorremos la lista del directorio
            if Directorio[i]["Telefono"] == telefono:#Comparamos los numeros
                print(Mensajes[12])
                print(f"\tNombre y apellido: {Directorio[i]['Nombre']}")
                print(f"\tTelefono celular: {Directorio[i]['Telefono']}")
                print(f"\tFecha de cumpleaños dd/mm: {Directorio[i]['Cumpleaños']}")
                print(f"\tCorreo electronico: {Directorio[i]['Correo']}")
                Directorio.remove(Directorio[i])#Eliminamos el diccionario que concida
                print(Mensajes[9])
                bucle = 0
                return
        print(Mensajes[10])

def Buscar_Persona():#Funcion para buscar persona
    bucle = 1#Inicializamos variable para crear un bucle
    while bucle == 1:#Creamos bucle en caso de no encontrar el numero
        telefono = int(input(Mensajes[11]))#Guardamos el numero que digito el usuario
        for i in range(len(Directorio)):#Recorremos la lista del directorio
            if Directorio[i]["Telefono"] == telefono:#Comparamos los numeros
                print(Mensajes[12])
                print(f"\tNombre y apellido: {Directorio[i]['Nombre']}")
                print(f"\tTelefono celular: {Directorio[i]['Telefono']}")
                print(f"\tFecha de cumpleaños dd/mm: {Directorio[i]['Cumpleaños']}")
                print(f"\tCorreo electronico: {Directorio[i]['Correo']}")
                bucle = 0
                return
        print(Mensajes[10])

#**************** Main ****************
print(Mensajes[0])

while True:
    opcion = int(input(Mensajes[6]))
    if opcion == 1:
        Agregar_Persona()
    elif opcion == 2:
        Borrar_Persona()
    elif opcion == 3:
        Buscar_Persona()
    elif opcion == 4:
        print(Mensajes[5])
        break
    else:
        print(Mensajes[13])