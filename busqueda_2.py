# en una lista tengo info sobre usuarios en forma de diccionarios
#las claves son dni, apellido (en mayusuculas), nombre (capitalizado), sueldo(float)
# ya hay 10 usuarios deben ser ingresados previamente

# armar menu 
# 1-me permita ingresar nuevos a usuarios 
# 2-buscar usuarios por dni 
# 0-sali
# Lista con 10 usuarios preexistentes
# Lista de diccionarios con 10 usuarios precargados
usuarios = [
    {"dni": "12345678", "apellido": "GOMEZ", "nombre": "Juan", "sueldo": 50000.0},
    {"dni": "23456789", "apellido": "PEREZ", "nombre": "Maria", "sueldo": 62000.5},
    {"dni": "34567890", "apellido": "LOPEZ", "nombre": "Carlos", "sueldo": 71000.0},
    {"dni": "45678901", "apellido": "FERNANDEZ", "nombre": "Ana", "sueldo": 48000.0},
    {"dni": "56789012", "apellido": "RODRIGUEZ", "nombre": "Luis", "sueldo": 55000.75},
    {"dni": "67890123", "apellido": "MARTINEZ", "nombre": "Laura", "sueldo": 59000.3},
    {"dni": "78901234", "apellido": "GARCIA", "nombre": "Diego", "sueldo": 64000.0},
    {"dni": "89012345", "apellido": "SANCHEZ", "nombre": "Lucia", "sueldo": 67000.9},
    {"dni": "90123456", "apellido": "RAMIREZ", "nombre": "Pedro", "sueldo": 72000.0},
    {"dni": "01234567", "apellido": "TORRES", "nombre": "Camila", "sueldo": 53000.0}
]

# Función que muestra el menú de opciones
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Ingresar nuevo usuario")  # Opción para agregar usuarios nuevos
    print("2. Buscar usuario por DNI")  # Opción para buscar usuario por su DNI
    print("0. Salir")  # Opción para salir del programa

# Función para ingresar un nuevo usuario a la lista
def ingresar_usuario():
    dni = input("Ingrese DNI: ")  # Solicita el DNI del nuevo usuario

    # Verifica si ya existe un usuario con ese DNI
    if any(u["dni"] == dni for u in usuarios):
        print("Ya existe un usuario con ese DNI.")  # Si existe, muestra mensaje
        return  # Sale de la función

    # Pide y guarda el apellido en mayúsculas
    apellido = input("Ingrese apellido (se guarda en mayúsculas): ").upper()

    # Pide y guarda el nombre capitalizado (primera letra en mayúscula)
    nombre = input("Ingrese nombre (se guarda capitalizado): ").capitalize()

    # Intenta convertir el sueldo a float
    try:
        sueldo = float(input("Ingrese sueldo: "))  # Solicita sueldo como número decimal
    except ValueError:  # Si no se puede convertir, se muestra error
        print("Sueldo inválido. No se ingresó el usuario.")
        return  # Sale de la función

    # Crea un nuevo diccionario con los datos ingresados
    nuevo_usuario = {
        "dni": dni,
        "apellido": apellido,
        "nombre": nombre,
        "sueldo": sueldo
    }

    usuarios.append(nuevo_usuario)  # Agrega el nuevo usuario a la lista
    print("Usuario agregado con éxito.")  # Muestra mensaje de confirmación

# Función para buscar un usuario por DNI
def buscar_usuario():
    dni = input("Ingrese DNI a buscar: ")  # Pide el DNI a buscar

    # Recorre la lista de usuarios
    for usuario in usuarios:
        if usuario["dni"] == dni:  # Si encuentra el DNI
            print(f"Usuario encontrado: {usuario}")  # Muestra los datos
            return  # Sale de la función

    print("No se encontró ningún usuario con ese DNI.")  # Si no lo encuentra

# Bucle principal del programa (menú interactivo)
while True:
    mostrar_menu()  # Muestra el menú cada vez que empieza el bucle

    opcion = input("Seleccione una opción: ")  # Pide al usuario elegir una opción

    if opcion == "1":
        ingresar_usuario()  # Llama a la función para ingresar usuario

    elif opcion == "2":
        buscar_usuario()  # Llama a la función para buscar por DNI

    elif opcion == "0":
        print("Saliendo del programa...")  # Muestra mensaje de salida
        break  # Sale del bucle (termina el programa)

    else:
        print("Opción inválida. Intente nuevamente.")  # Si la opción es incorrecta
