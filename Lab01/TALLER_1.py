directorio = []

mensajes = [
    "Bienvenido al directorio telefónico.",
    "Digite el nombre y apellido de la persona: ",
    "Digite el teléfono celular de la persona: ",
    "Digite el cumpleaños de la persona (DD/MM/AAAA): ",
    "Digite el correo electrónico de la persona: ",
    "Registro agregado exitosamente.",
    "No se encontró ninguna persona con ese teléfono.",
    "Registro eliminado exitosamente.",
    "Saliendo del programa...",
    "Opción no válida, por favor intente de nuevo.",
    "El número de teléfono debe tener exactamente 10 dígitos.",
    "Formato de fecha incorrecto. Use el formato DD/MM/AAAA."
]

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar un nuevo registro")
    print("2. Buscar una persona por teléfono celular")
    print("3. Borrar un registro")
    print("4. Salir de la aplicación")

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 10

def validar_fecha(fecha):
    if len(fecha) == 10 and fecha[2] == '/' and fecha[5] == '/':
        dia, mes, anio = fecha.split('/')
        return dia.isdigit() and mes.isdigit() and anio.isdigit()
    return False

def agregar_registro():
    persona = {}
    print(mensajes[1])
    persona['nombre'] = input()
    while True:
        print(mensajes[2])
        telefono = input()
        if validar_telefono(telefono):
            persona['telefono'] = int(telefono)
            break
        else:
            print(mensajes[10])  
    while True:
        print(mensajes[3])
        cumpleanos = input()
        if validar_fecha(cumpleanos):
            persona['cumpleanos'] = cumpleanos
            break
        else:
            print(mensajes[11])  
    print(mensajes[4])
    persona['correo'] = input()
    directorio.append(persona)
    print(mensajes[5])  

def buscar_por_telefono():
    while True:
        print("Digite el teléfono celular a buscar: ")
        telefono = input()
        if validar_telefono(telefono):
            telefono = int(telefono)
            break
        else:
            print(mensajes[10])    
    for persona in directorio:
        if persona['telefono'] == telefono:
            print(f"Nombre: {persona['nombre']}")
            print(f"Teléfono: {persona['telefono']}")
            print(f"Cumpleaños: {persona['cumpleanos']}")
            print(f"Correo: {persona['correo']}")
            return
    print(mensajes[6])  

def borrar_registro():
    while True:
        print("Digite el teléfono celular del registro a borrar: ")
        telefono = input()
        if validar_telefono(telefono):
            telefono = int(telefono)
            break
        else:
            print(mensajes[10])  
    for persona in directorio:
        if persona['telefono'] == telefono:
            directorio.remove(persona)
            print(mensajes[7])  
            return
    print(mensajes[6]) 

def main():
    print(mensajes[0])  
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion in ['1', '2', '3', '4']:
            if opcion == '1':
                agregar_registro()
            elif opcion == '2':
                buscar_por_telefono()
            elif opcion == '3':
                borrar_registro()
            elif opcion == '4':
                print(mensajes[8])  
                break
        else:
            print(mensajes[9]) 
             
if __name__ == "__main__":
    main()