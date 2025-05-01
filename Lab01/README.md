[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18698265&assignment_repo_type=AssignmentRepo)

[![Universidad ECCI][IMGECCI]][ECCIBOG]

# lab01-Listas-Diccionarios

Cada integrante realizo el laboratorio individualmente.

## Integrantes
| Integrantes |
| - |
| [`Diego Lopez`][Alejo] |
| [`Daniel Ramirez`][Daniel]||
| [`Sebastian Martinez`][Sebas]||
||

## Documentación

En [TALLER1](lab01-listas-y-diccionarios-g4/TALLER1.pdf) se requiere un codigo en PYTHON el cual permita gestionar un directorio telefonico de un grupo de personas x, a traves de listas y diccionarios.

| **Integrante** | **Enlace** | **Repositorios** |
|-|-|-|
| **Daniel Ramirez** | [Taller 1 Daniel](/TALLER%201%20LISTAS%20Y%20DICCIONARIOS%20DANIEL%20RAMIREZ.py) | [Repolab1 Daniel](https://github.com/D4N1EL-R4M1R3Z/SISTEMAS-DIGITALES-III/tree/main/TALLER%201) |
| **Sebastian Martinez** |  [Taller 1 Sebastian](/TALLER_1.py)| [Repolab1 Sebastian](https://github.com/SebasMtz30/SDigitales_III/tree/main/LAB_1) |
| **Diego Lopez** | [Taller 1 Diego](/Directorio_Telefonico.py)|[RepoLab1 Diego](https://github.com/Alejibiris/Sistemas-Digitales-III/tree/main/Laboratorio1) |

## Descripción del Programa
Este programa es una aplicación de consola en Python que permite gestionar un directorio telefónico. Los usuarios pueden agregar, buscar y eliminar registros de personas, almacenando información como:

- Nombre y apellido

- Teléfono celular

- Cumpleaños

- Correo electrónico

El programa utiliza listas para almacenar los registros y diccionarios para estructurar la información de cada persona. Además, se emplean mensajes predefinidos para guiar al usuario durante la ejecución.

## Estructura del Código
El programa está organizado en las siguientes partes:

1. Listas:

- directorio: Almacena los registros de las personas (cada registro es un diccionario).

- mensajes: Contiene los textos que se muestran en pantalla (bienvenida, solicitudes de datos, confirmaciones, etc.).

2. Funciones:

- mostrar_menu(): Muestra un menú con las opciones disponibles.

- agregar_registro(): Permite al usuario agregar un nuevo registro al directorio.

- buscar_por_telefono(): Busca una persona por su número de teléfono y muestra su información.

- borrar_registro(): Elimina un registro basado en el número de teléfono.

- main(): Función principal que controla el flujo del programa.

3. Flujo del Programa:

- Se muestra un menú con las opciones disponibles para el usuario.

  ![Menu principal]( /Imagenes/Menu_Principal.png)
  

- Luego solicita el nombre de la persona, valida el número de teléfono. Si no es válido, muestra un mensaje de error y pide el teléfono nuevamente.

  ![Mensaje error](/Imagenes/Mensaje_Telefono.png)

  Valida la fecha de cumpleaños. Si no es válida, muestra un mensaje de error y pide la fecha nuevamente, solicita el correo electrónico y almacena el registro en la lista directorio y muestra un mensaje de confirmación.

  ![Registro](/Imagenes/Registro.png)

- Para buscar el registro valida el número de teléfono. Si no es válido, muestra un mensaje de error y pide el teléfono nuevamente y si encuentra la persona, muestra su información. Si no, muestra un mensaje de error.

    ![Buscar Registro](/Imagenes/Buscar_Registro.png)

- Para borrar el registro valida el número de teléfono. Si no es válido, muestra un mensaje de error y pide el teléfono nuevamente. Si encuentra la persona, la elimina de la lista y muestra un mensaje de confirmación. Si no, muestra un mensaje de error.

  ![Eliminar Registro](/Imagenes/Borrar_Registro.png)

## Detalles Adicionales
- Persistencia de Datos: Los datos se almacenan en memoria (en una lista) durante la ejecución del programa. Si se cierra el programa, los datos se pierden. 

- Validaciones: El programa no incluye validaciones avanzadas (por ejemplo, verificar si el teléfono ya existe o si el correo tiene un formato válido). Esto se podría implementar en futuras versiones.

- Interfaz de Usuario: El programa es una aplicación de consola, por lo que no tiene una interfaz gráfica.

## Cómo se Podría Emplear en la Vida Real
Este programa es útil en situaciones donde se necesita gestionar un pequeño directorio de contactos de manera rápida y sencilla. Algunos casos de uso podrían ser:

1. Uso Personal:

- Mantener un registro de contactos personales (familiares, amigos, colegas).

- Buscar rápidamente el número de teléfono o correo de una persona.

2. Pequeñas Empresas:

- Gestionar los contactos de clientes o proveedores.

- Tener a mano la información de contacto clave para comunicarse rápidamente.

3. Educación:

- Como herramienta de aprendizaje para estudiantes que están comenzando a programar en Python.

- Ejemplo práctico de cómo usar listas, diccionarios y funciones en un proyecto real.

## Ejemplo de Uso en la Vida Real
Imagina que eres el organizador de un evento y necesitas mantener un registro de los participantes. Con este programa, se puede:

- Agregar a cada participante con su nombre, teléfono, cumpleaños y correo.

- Buscar rápidamente a un participante por su número de teléfono si necesitas contactarlo.

- Eliminar a un participante si ya no asistirá al evento.

- Este tipo de herramienta es especialmente útil cuando no se tiene acceso a software más complejo (como una base de datos) y se necesita una solución rápida y eficiente.

## Conclusión
Este programa es un ejemplo sencillo pero efectivo de cómo se pueden utilizar listas y diccionarios en Python para resolver problemas del mundo real. Aunque es básico, puede ser ampliado con funcionalidades adicionales (como guardar los datos en un archivo o agregar validaciones) para adaptarse a necesidades más específicas.

[//]: # (Referencias)

[Alejo]: <https://github.com/Alejibiris>
[Daniel]: <https://github.com/D4N1EL-R4M1R3Z>
[Sebas]: <https://github.com/SebasMtz30>
[ECCIBOG]: <https://www.ecci.edu.co/bogota/>
[IMGECCI]: <https://www.ecci.edu.co/wp-content/uploads/2021/11/logo-ECCI.png>
