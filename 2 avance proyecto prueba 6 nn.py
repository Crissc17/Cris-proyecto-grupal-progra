import json

def mostrar_menu():


    print("Menu de Tareas:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Editar o borrar tareas")
    print("5. Guardar tareas")
    print("6. Cargar tareas")
    print("7. Ver estadísticas")
    print("8. Salir")

def agregar_tarea(tareas):
    titulo = input("Ingrese el título de la nueva tarea: ")
    descripcion = input("Ingrese la descripción de la nueva tarea: ")
    fecha = input("Ingrese la fecha de la tarea (formato: dd/mm/yyyy): ")
    while not validar_formato_fecha(fecha):
        print("Formato de fecha incorrecto. Por favor, ingrese la fecha en formato dd/mm/yyyy.")
        fecha = input("Ingrese la fecha de la tarea (formato: dd/mm/yyyy): ")
    costo = float(input("Ingrese el costo de la tarea: "))
    completada = False
    nueva_tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha": fecha,
        "costo": costo,
        "completada": completada
    }
    tareas.append(nueva_tarea)
    print("Tarea agregada con éxito.")

def validar_formato_fecha(fecha):
    try:
        dia, mes, anio = fecha.split("/")
        if len(anio) == 4 and len(mes) == 2 and len(dia) == 2:
            int(dia)
            int(mes)
            int(anio)
            return True
        else:
            return False
    except ValueError:
        return False

def ver_tareas(tareas):
    if not tareas:
        print("Todavía no hay tareas agregadas.")
    else:
        print("Tareas:")
        for i, tarea in enumerate(tareas, 1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}.")
            print(f"   Título: {tarea['titulo']}")
            print(f"   Descripción: {tarea['descripcion']}")
            print(f"   Fecha: {tarea['fecha']}")
            print(f"   Costo: ${tarea['costo']}")
            print(f"   Estado: {estado}")

def marcar_completada(tareas):
    if not tareas:
        print("Todavía no hay tareas para marcar como completadas.")
        return

    ver_tareas(tareas)
    tarea_desc = input("Ingrese el título de la tarea completada: ")
    for tarea in tareas:
        if tarea["titulo"] == tarea_desc:
            tarea["completada"] = True
            print("Tarea marcada como completada.")
            return

    print("No se encontró la tarea especificada.")

def guardar_tareas(tareas):
    with open('tareas.json', 'w') as file:
        json.dump(tareas, file)
    print("Tareas guardadas con éxito.")

def cargar_tareas(nombre_archivo='tareas.json'):
    try:
        with open(nombre_archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"No se encontró el archivo de tareas: {nombre_archivo}.")
        return []
    except json.decoder.JSONDecodeError:
        print(f"El archivo de tareas está vacío o no es válido: {nombre_archivo}.")
        return []
def editar_tarea(tareas):
    if not tareas:
        print("Todavía no hay tareas agregadas.")
        return []

    ver_tareas(tareas)
    tarea_desc = input("Ingrese el título de la tarea que desea editar: ")
    for tarea in tareas:
        if tarea["titulo"] == tarea_desc:
            nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
            tarea["descripcion"] = nueva_descripcion
            print("Tarea editada con éxito.")
            return

    print("No se encontró la tarea especificada.")

def borrar_tarea(tareas):
    if not tareas:
        print("Todavía no hay tareas agregadas.")
        return []

    ver_tareas(tareas)
    tarea_desc = input("Ingrese el título de la tarea que desea borrar: ")
    for tarea in tareas:
        if tarea["titulo"] == tarea_desc:
            tareas.remove(tarea)
            print("Tarea borrada con éxito.")
            return tareas

    print("No se encontró la tarea especificada.")
    return tareas
def mostrar_tareas_guardadas(tareas):
    if not tareas:
        print("No hay tareas guardadas.")
    else:
        print("Tareas guardadas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. Título: {tarea['titulo']}")
            print(f"   Descripción: {tarea['descripcion']}")
            print(f"   Fecha: {tarea['fecha']}")
            print(f"   Costo: ${tarea['costo']}")
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"   Estado: {estado}")
            print()

def cargar_tareas():
    try:
        with open('tareas.json', 'r') as file:
            tareas_guardadas = json.load(file)
            mostrar_tareas_guardadas(tareas_guardadas)
            return tareas_guardadas
    except FileNotFoundError:
        print("No se encontró el archivo de tareas.")
        return []
    except json.decoder.JSONDecodeError:
        print("El archivo de tareas está vacío o no es válido.")
        return []

def ver_estadisticas(tareas):
    total_tareas = len(tareas)
    total_completadas = sum(1 for tarea in tareas if tarea["completada"])
    total_pendientes = total_tareas - total_completadas
    costo_pendientes = sum(tarea["costo"] for tarea in tareas if not tarea["completada"])
    costo_completadas = sum(tarea["costo"] for tarea in tareas if tarea["completada"])
    costo_total = costo_pendientes + costo_completadas

    print("Estadísticas:")
    print(f"Número total de tareas: {total_tareas}")
    print(f"Número total de tareas pendientes: {total_pendientes}")
    print(f"Número total de tareas completadas: {total_completadas}")
    print(f"Total de costo de tareas pendientes: ${costo_pendientes}")
    print(f"Total de costo de tareas completadas: ${costo_completadas}")
    print(f"Total de costo de tareas (pendientes y completadas): ${costo_total}")

def main():
    tareas = cargar_tareas()
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción: ")
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            print("Seleccione la operación:")
            print("a. Editar tarea")
            print("b. Borrar tarea")
            operacion = input("Ingrese la letra de la operación que desea realizar: ")
            if operacion == "a":
                editar_tarea(tareas)
            elif operacion == "b":
                tareas = borrar_tarea(tareas)
            else:
                print("Operación inválida.")
        elif opcion == "5":
            guardar_tareas(tareas)
        elif opcion == "6":
            tareas = cargar_tareas()
        elif opcion == "7":
            ver_estadisticas(tareas)
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 8.")

if __name__ == "__main__":
    main()
