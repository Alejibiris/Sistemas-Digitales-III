# Importamos librerias necesarias
import json # Manejar archivos JSON
import re # Validar datos ingresados
from datetime import datetime # Manejar datos en tipo fechas

# Clase para crear un contacto con sus atributos principales
class Contacto:
    # Metodo para agregar atributos al contacto
    def __init__(self, Id, nombre, telefono, fecha_nacimiento, correo, area):
        self.Id = Id
        self.nombre = nombre
        self.telefono = telefono
        self. fecha_nacimiento =  fecha_nacimiento
        self.correo = correo
        self.area = area
    
    # Metodo para representar en texto el contacto
    def __str__(self):
        return f" Tu ID es: {self.Id} \n Nombre: {self.nombre} \n telefono {self.telefono} \n Naciste: {self.fecha_nacimiento} \n Tu correo {self.correo}\n Tu area: {self.area}"

# Clase para crear el directorio de los datos
class Directorio:
    # Inicializamos el directorio cargando los datos de JSON
    def __init__(self):
        self.contactos = []# Lista de contactos
        self.indice_telefonos = {}# Diccionario de telefonos para la busqueda
        self.indice_ids = {}# Diccionario de id's para la busqueda
        self.indice_areas = {}# Diccionario de areas para la busqueda
        self.areas = ["Recursos Humanos", "Redes", "CiberSeguridad", "Produccion"]# Lista de areas predefinidas
        self.Importar_Datos()# Funcion para importar datos de JSON

    # Funcion para importar datos de JSON
    def Importar_Datos(self):
        # Importamos los contactos de JSON
        try:
            # Abrimos el archivo JSON en modo lectura
            with open("ContactosJSON.json", "r") as Ar_JOSN:
                Personas = json.load(Ar_JOSN)

                # Separamos cada objeto de la lista y agregamos c/u a su diccionario de contactos
                for item in Personas:
                    self.agregar_contacto(item['Id'], item['nombre'], item['telefono'], item['fecha_nacimiento'], item['correo'], item['area'])
        except FileNotFoundError:
            pass
    
    # Funcion para exportar los datos nuevos a JSON
    def Exportar_Datos(self):
        # Abrimos el archivo JSON en modo escritura
        with open("ContactosJSON.json", "w") as Ar_JOSN:
            # Con la lista de contactos lo pasamos a tipo diccionario para con .dump pasarlo a datos tipo JSON que es una lista de diccionarios
            json.dump([contacto.__dict__ for contacto in self.contactos], Ar_JOSN)
    
    # Funcion para agregar los contactos al local y archivo JSON
    def agregar_contacto(self, id, nombre, telefono, fecha_nacimiento, correo, area):
        # Validamos los datos ingresados (Telefono, Correo y fecha de nacimiento)
        if not self.validar_telefono(telefono):
            print("Telefono invalido. Contacto no agregado.")
            return
        if not self.validar_correo(correo):
            print("Correo invalido. Contacto no agregado.")
            return
        if not self.validar_fecha_nacimiento(fecha_nacimiento):
            print("Fecha de nacimiento invalida. Contacto no agregado.")
            return
        
        # Si los datos son validos los agregamos
        contacto = Contacto(id, nombre, telefono, fecha_nacimiento, correo, area)
        self.contactos.append(contacto)
        self.indice_telefonos[telefono] = contacto
        self.indice_ids[id] = contacto
        # Si el area es nueva la agrega a la lista de areas y añade el contacto
        self.indice_areas.setdefault(area, []).append(contacto)
        # Subimos el contacto al archivo JSON
        self.Exportar_Datos()

    # Funciones tipo static para usarlas dentro de la misma clase
    @staticmethod
    def validar_telefono(telefono):
        # Valida que el teléfono tenga exactamente 10 dígitos de 0 a 9 c/u 
        return bool(re.fullmatch(r"\d{10}", telefono))
    
    @staticmethod
    def validar_correo(correo):
        # Valida que el correo tenga un formato correcto("Texto"@"Texto"."Texto")
        return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo))
    
    @staticmethod
    def validar_fecha_nacimiento(fecha):
        # Valida que la fecha de nacimiento esté en formato YYYY-MM-DD
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    # Funcion para mostrar los contactos almacenados
    def mostrar_contactos(self):
        # Muestra la lista de contactos orden alfabetico por nombre con sorted y su clave lambda
        for contacto in sorted(self.contactos, key=lambda x: x.nombre):
            print(contacto)

    # Funciones para buscar un contacto 
    def buscar_por_telefono(self, telefono):
        # Busca un contacto por número de teléfono
        return self.indice_telefonos.get(telefono, "No encontrado")
    
    def buscar_por_id(self, id):
        # Busca un contacto por ID
        return self.indice_ids.get(id, "No encontrado")
    
    def buscar_por_area(self, area):
        # Devuelve la lista de contactos que permanescan a esa area
        return self.indice_areas.get(area, [])
    
    # Funciones para eliminar un contacto
    def eliminar_contacto_id(self, id):
        # Elimina un contacto por su ID
        if id in self.indice_ids:
            contacto = self.indice_ids.pop(id)
            self.contactos.remove(contacto)
            self.indice_telefonos.pop(contacto.telefono, None)
            self.indice_areas[contacto.area].remove(contacto)
            self.Exportar_Datos()
            return True
        return False
    
    def eliminar_contacto_tel(self, telefono):
        # Elimina un contacto por su número de teléfono
        if telefono in self.indice_telefonos:
            contacto = self.indice_telefonos.pop(telefono)
            self.contactos.remove(contacto)
            self.indice_ids.pop(contacto.id, None)
            self.indice_areas[contacto.area].remove(contacto)
            self.Exportar_Datos()
            return True
        return False
    
# Funcion para manejar el menu de la terminal
def menu():
    # Iniciamos el directorio
    directorio = Directorio()
    while True:
        print("\n\t----Menu----\n1. Agregar contacto\n2. Buscar por telefono\n3. Buscar por ID\n4. Buscar por area\n5. Eliminar por ID\n6. Eliminar por telefono\n7. Mostrar contactos\n8. Salir")
        opcion = int(input("\n\t--Seleccione una opcion: "))

        if opcion == 1:
            id = input("ID: ")
            nombre = input("Nombre: ")
            telefono = input("Telefono: ")
            fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
            correo = input("Correo: ")
            area = input("Area: ")
            directorio.agregar_contacto(id, nombre, telefono, fecha_nacimiento, correo, area)
        elif opcion == 2:
            telefono = input("Telefono: ")
            print(directorio.buscar_por_telefono(telefono))
        elif opcion == 3:
            id = input("ID: ")
            print(directorio.buscar_por_id(id))
        elif opcion == 4:
            area = input("area: ")
            for persona in directorio.buscar_por_area(area):
                print(persona)
        elif opcion == 5:
            id = input("ID: ")
            if directorio.eliminar_contacto_id(id):
                print("Contacto eliminado.")
            else:
                print("ID no encontrado.")
        elif opcion == 6:
            telefono = input("Telefono: ")
            if directorio.eliminar_contacto_tel(telefono):
                print("Contacto eliminado.")
            else:
                print("Telefono no encontrado.")
        elif opcion == 7:
            directorio.mostrar_contactos()
        elif opcion == 8:
            break
        else:
            print("Opcion no valida.")

# Iniciamos el programa
if __name__ == "__main__":
    menu()
