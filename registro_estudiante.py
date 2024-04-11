#registro de estudiantes 3

mi_diccionario = {}
import os
os.system('cls')
sw = True

def fnt_agregar(mi_diccionario, nombre, edad, carrera):
    if nombre == '' or edad == '' or carrera == '':
        enter = input('Debe diligenciar toda la información solicitada >ENTER<')
    else:
        mi_diccionario[nombre] = {'EDAD': edad, 'CARRERA': carrera}
        enter = input('\n\nEl estudiante ha sido registrado <ENTER>')       
        
def fnt_registro():
    os.system('cls')
    nombre = input('Ingrese su nombre:  ') 
    edad = input('Ingrese su edad:   ')
    carrera = input('Ingrese su carrera:  ')
    fnt_agregar(mi_diccionario, nombre, edad, carrera)
    
def fnt_buscar():
    if buscar in mi_diccionario:
        print(mi_diccionario[buscar])
    else:
        print('El estudiante no se encuentra registrado')
    

while sw == True:   
    opcion = input('1. REGISTRAR\n2. BUSCAR\n3. SALIR\n->')
    os.system('cls')
    if opcion == '1':
        fnt_registro()
        os.system('cls')
    if opcion == '2':
        os.system('cls')
        buscar =input('Ingrese el nombre del estudiante:  ')
        os.system('cls')
        fnt_buscar()
    if opcion == '3':
        sw = False
   