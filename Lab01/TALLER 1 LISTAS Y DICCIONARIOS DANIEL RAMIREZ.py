# Taller 1 - Sistemas Digitales III - Daniel Ramirez

# Elaborar un programa como DIRECTORIO TELEFONICO

# Declaramos la variable bandera para continuar o finalizar la ejecución del programa
FLAG = 1  # De manera que el ciclo siempre se ejecute hasta que sea False
OP = 0  # Variable para seleccionar opción

# Creamos la lista que va a ser la que almacene los diccionarios con los datos registrados
DIRECTORIO = []

# Lista que almacena los textos que se mostrarán en pantalla
TEXTO_PANTALLA = [
    "Hola como estas !!!!",
    "Digita el Nombre y Apellido: ",
    "Digita el Teléfono Celular: ",
    "Digita el Cumpleaños: ",
    "Digita el Correo: ",
    "Esto fue todo por este registro"
]

# Creamos la función Menú con las 4 opciones solicitadas
def MENU():
    print("____________________________")
    print("Ingresaste al MENU PRINCIPAL")
    print("----------------------------")
    print("Por favor Elige una opción: \n")
    print("1. Agregar un nuevo registro")
    print("2. Buscar una persona por teléfono celular")
    print("3. Borrar un registro")
    print("4. Salir de la aplicación.")
    print("______________________________________________________")
    
    try:
        OPCION = int(input("Por favor elija una opción: "))
    except ValueError:
        OPCION = -1  # Valor inválido
    
    if 1 <= OPCION <= 4:
        return OPCION
    else:
        return -1

# Creamos la función para los diccionarios que se guarden en DIRECTORIO
def NUEVO_REGISTRO():
    print("~~~~~ AGREGA EL NUEVO REGISTRO ~~~~~\n")

    ELEMENTO = {
        "NOMBRE Y APELLIDO": input(TEXTO_PANTALLA[1]).title(),
        "Telefono Celular": input(TEXTO_PANTALLA[2]),
        "CUMPLEAÑOS": input(TEXTO_PANTALLA[3]),
        "CORREO": input(TEXTO_PANTALLA[4])
    }

    DIRECTORIO.append(ELEMENTO)
    print("Registro agregado correctamente.\n")

# Función para buscar una persona por el numero de telefono
def BUSCAR_REGISTRO():
    telefono = input("Ingrese el teléfono a buscar: ")
    for persona in DIRECTORIO:
        if persona["Telefono Celular"] == telefono:
            print("Registro encontrado:")
            print(persona)
            return
    print("No se encontró ningún registro con ese telefono.\n")

# Función para borrar un registro por numero de telefono
def BORRAR_REGISTRO():
    telefono = input("Ingrese el teléfono del registro a borrar: ")
    for persona in DIRECTORIO:
        if persona["Telefono Celular"] == telefono:
            DIRECTORIO.remove(persona)
            print("Registro eliminado correctamente.\n")
            return
    print("No se encontró ningún registro con ese telefono.\n")

# Bucle principal del programa
print(TEXTO_PANTALLA[0])  # Mensaje de bienvenida
while FLAG:
    OP = MENU()
    if OP == 1:
        NUEVO_REGISTRO()
    elif OP == 2:
        BUSCAR_REGISTRO()
    elif OP == 3:
        BORRAR_REGISTRO()
    elif OP == 4:
        FLAG = 0
        print(TEXTO_PANTALLA[5])  # Mensaje de despedida
    else:
        print("Opción inválida. Por favor, intente de nuevo.\n")
