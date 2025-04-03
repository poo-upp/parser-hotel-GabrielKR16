# Importamos las clases y funciones necesarias
from reserva1 import Cliente, HabitacionDoble, Suite 
from datetime import datetime, timedelta  
import sys

# Si es necesario, agregamos la ruta donde se encuentra el archivo 'reserva1.py'
sys.path.append(r"C:\Users\jenni\OneDrive\Escritorio\gabriel tareas\pouuuu")

# Función para leer la información de la reserva desde un archivo
def leer_reserva(archivo):
    """
    Lee un archivo de texto y extrae la información de la reserva.
    Retorna un objeto Cliente, número de noches, fecha de inicio y lista de habitaciones.
    """
    cliente, num_noches, fecha_inicio = None, 0, ""  # Inicializamos las variables
    habitaciones = []  # Lista para almacenar las habitaciones reservadas
    # Diccionario que mapea los nombres de las habitaciones con las clases correspondientes
    habitaciones_disponibles = {"habitacion doble": HabitacionDoble, "suite": Suite}

    # Abrimos el archivo de texto en modo lectura
    with open(archivo, 'r', encoding="utf-8") as file:
        # Leemos cada línea del archivo
        for line in file:
            line = line.strip().lower()  # Eliminamos espacios y pasamos a minúsculas

            # Si encontramos la línea que contiene el nombre del cliente
            if "nombre del cliente" in line:
                cliente = Cliente(next(file).strip(), "-")  # Leemos el siguiente dato como nombre del cliente

            # Si encontramos la línea con el correo del cliente y ya tenemos un cliente
            elif "correo" in line and cliente:
                cliente.correo = line.split()[-1]  # Extraemos el correo de la línea

            # Si encontramos la línea con el número de noches
            elif "numero de noches" in line:
                num_noches = int(line.split()[-1])  # Extraemos el número de noches

            # Si encontramos la línea con la fecha de inicio de la reserva
            elif "fecha inicio" in line:
                fecha_inicio = line.split()[-1]  # Extraemos la fecha de inicio

            # Si la línea coincide con alguna de las habitaciones disponibles
            elif line in habitaciones_disponibles:
                habitaciones.append(habitaciones_disponibles[line](len(habitaciones) + 1))  # Añadimos la habitación correspondiente

    # Devolvemos el cliente, el número de noches, la fecha de inicio y la lista de habitaciones
    return cliente, num_noches, fecha_inicio, habitaciones


# Función para generar el resumen de la reserva y guardarlo en un archivo
def generar_resumen_reserva(cliente, noches, fecha, habitaciones):
    """
    Genera un resumen de la reserva y lo guarda en un archivo.
    """
    # Calculamos la fecha de check-out sumando las noches a la fecha de check-in
    fecha_checkout = (datetime.strptime(fecha, "%d-%m-%Y") + timedelta(days=noches)).strftime("%d-%m-%Y")

    # Diccionario para contar las habitaciones por tipo
    habitacion_contador = {"Habitacion doble": 0, "Suite": 0}
    # Contamos las habitaciones según su tipo
    for hab in habitaciones:
        nombre_hab = "Habitacion doble" if isinstance(hab, HabitacionDoble) else "Suite"
        habitacion_contador[nombre_hab] += 1

    # Precios por tipo de habitación
    precios = {"Habitacion doble": 900, "Suite": 2000}

    # Calculamos el precio total multiplicando el número de habitaciones por su precio y las noches
    total_precio = sum(habitacion_contador[nombre] * precios[nombre] for nombre in precios) * noches

    # Abrimos el archivo de salida en modo escritura
    with open("output.txt", "w", encoding="utf-8") as out:
        # Escribimos la información del cliente y la reserva
        out.write(f"¡Hola {cliente.nom}! Aquí tienes los detalles de tu reserva:\n\n")
        out.write(f"Check-in:\t{fecha}\nCheck-out:\t{fecha_checkout}\n\n")
        out.write(f"Reservaste\t{noches} noches, {len(habitaciones)} habitaciones, {sum(h.capacidad for h in habitaciones)} personas\n\n")

        # Escribimos los detalles de las habitaciones reservadas
        out.write("Detalles de reserva\n")
        for nombre, cantidad in habitacion_contador.items():
            if cantidad:
                out.write(f"[{cantidad}]\t{nombre}\n")

        # Escribimos los detalles del contacto y los precios
        out.write(f"\nE-mail de contacto\t[{cliente.correo}]\n\nDetalles del precio:\n")
        for nombre, cantidad in habitacion_contador.items():
            if cantidad:
                precio_total = cantidad * precios[nombre] * noches
                out.write(f"[{cantidad}]\t{nombre}\t\t {precio_total:.2f}$\n")

        # Escribimos el total de la reserva
        out.write("----------------------------------------------\n")
        out.write(f"Total:\t\t\t\t\t{total_precio:.2f}$\n")

# Archivo de entrada, ruta al archivo que contiene la reserva
documento = r"C:\Users\jenni\OneDrive\Escritorio\gabriel tareas\pouuuu\INPUT.txt"

# Llamamos a la función para leer la reserva
cliente, noches, fecha, habitaciones = leer_reserva(documento)

# Si encontramos un cliente, generamos el resumen
if cliente:
    generar_resumen_reserva(cliente, noches, fecha, habitaciones)
    print("Resumen generado en 'output.txt'.")  # Imprimimos mensaje de éxito
else:
    print("No se encontró información del cliente.")  # Imprimimos mensaje de error
