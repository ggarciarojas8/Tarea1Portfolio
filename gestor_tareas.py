# Función para agregar una nueva actividad a la lista de actividades
def agregar_actividad(actividad, lista_actividades):
    lista_actividades.append(actividad)
    print("Actividad agregada exitosamente.")

# Función para mostrar todas las actividades en la lista
def mostrar_actividades(lista_actividades):
    if lista_actividades:
        print("Lista de actividades:")
        for i, actividad in enumerate(lista_actividades, start=1):
            print(f"{i}. {actividad}")
    else:
        print("No hay actividades pendientes por comprar.")

# Función para marcar una actividad como comprada
def comprar_actividad(numero_actividad, lista_actividades):
    if 1 <= numero_actividad <= len(lista_actividades):
        actividad_comprada = lista_actividades.pop(numero_actividad - 1)
        print(f"actividad '{actividad_comprada}' comprada.")
    else:
        print("Número de actividad inválido.")

# Función para guardar las actividades en un archivo de texto
def guardar_actividades(nombre_archivo, lista_actividades):
    try:
        with open(nombre_archivo, 'w') as archivo:
            for actividad in lista_actividades:
                archivo.write(actividad + '\n')
        print("actividades guardadas en el archivo correctamente.")
    except IOError:
        print("Error al guardar las tareas en el archivo.")
# Lista para almacenar las actividades
actividades = []

# Menú principal
while True:
    print("\n--- GESTIÓN DE ACTIVIDADES ---")
    print("1. Agregar actividad")
    print("2. Mostrar actividades")
    print("3. Comprar actividades")
    print("4. Guardar actividades")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción que desea: ")

    if opcion == '1':
        nueva_actividad = input("Ingrese la nueva actividad: ")
        agregar_actividad(nueva_actividad, actividades)
    elif opcion == '2':
        mostrar_actividades(actividades)
    elif opcion == '3':
        if actividades:
            mostrar_actividades(actividades)
            num_actividad_comprada = int(input("Ingrese el número de la actividad comprada: "))
            comprar_actividad(num_actividad_comprada, actividades)
        else:
            print("No hay actividades para comprar.")
    elif opcion == '4':
        nombre_archivo = input("Ingrese el nombre del archivo para guardar las actividades: ")
        guardar_actividades(nombre_archivo, actividades)
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")