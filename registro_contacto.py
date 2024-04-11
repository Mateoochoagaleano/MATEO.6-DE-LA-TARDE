#Ejercicio 1: Registro de Contactos
#Enunciado:
#Escribe un programa en Python que permita al usuario registrar contactos. El programa debe
#permitir al usuario ingresar el nombre y el número de teléfono de cada contacto. Luego, el programa
#debe permitir al usuario buscar un contacto por su nombre y mostrar su número de teléfono
#correspondiente.



import os



def registrar_contacto(agenda):
    os.system('cls')
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[nombre] = telefono
    input(f"Contacto '{nombre}' registrado con éxito.\n")

def buscar_contacto(agenda):
    os.system('cls')
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"El número de teléfono de '{nombre}' es: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.\n")
    input('')

def main():
    agenda = {}
    while True:
        os.system('cls')
        print("Bienvenido a la agenda de contactos.")
        print("1. Registrar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Salir")
        opcion = input("Ingrese una opción (1/2/3): ")

        if opcion == '1':
            registrar_contacto(agenda)
        elif opcion == '2':
            buscar_contacto(agenda)
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese 1, 2 o 3.\n")

if __name__ == "_main_":
    main()
