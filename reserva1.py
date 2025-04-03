# Importa el módulo 'date' de la librería 'datetime', que se usará para trabajar con fechas.
from datetime import date

# Clase base Habitacion que representa cualquier tipo de habitación en el hotel
class Habitacion:
    def __init__(self, numero, capacidad, precio, disponible=True):
        # Inicializa los atributos básicos de la habitación: número, capacidad, precio y estado de disponibilidad.
        self.numero = numero  # Número de la habitación
        self.capacidad = capacidad  # Capacidad de personas que puede alojar
        self.precio = precio  # Precio por noche de la habitación
        self._disponible = disponible  # Atributo privado para manejar la disponibilidad de la habitación

    @property
    def disponible(self):
        # Método para obtener el estado de disponibilidad de la habitación.
        return self._disponible

    @disponible.setter
    def disponible(self, estado):
        # Método para modificar el estado de disponibilidad de la habitación.
        self._disponible = estado

    def __eq__(self, otra):
        # Compara dos habitaciones en función de su número, capacidad y precio.
        return (self.numero == otra.numero and
                self.capacidad == otra.capacidad and
                self.precio == otra.precio)

    def __add__(self, otra):
        # Método que permite sumar los precios de dos habitaciones, para obtener un costo total.
        return self.precio + otra.precio


# Clase HabitacionSimple con características específicas
# Representa una habitación simple que tiene una capacidad para 1 persona y un precio fijo
class HabitacionSimple(Habitacion):
    def __init__(self, numero):
        # Llama al constructor de la clase base con los valores específicos para esta habitación (capacidad=1, precio=500).
        super().__init__(numero, capacidad=1, precio=500)


# Clase HabitacionDoble con características específicas
# Representa una habitación doble que tiene una capacidad para 2 personas y un precio fijo
class HabitacionDoble(Habitacion):
    def __init__(self, numero, balcon=False):
        # Llama al constructor de la clase base con los valores específicos para esta habitación (capacidad=2, precio=900).
        super().__init__(numero, capacidad=2, precio=900)
        self.balcon = balcon  # Atributo adicional para definir si la habitación tiene balcón


# Clase Suite con opción adicional de jacuzzi
# Representa una suite que tiene una capacidad para 4 personas y un precio base más alto
class Suite(Habitacion):
    def __init__(self, numero, jacuzzi=False):
        # Llama al constructor de la clase base con los valores específicos para esta habitación (capacidad=4, precio=2000).
        super().__init__(numero, capacidad=4, precio=2000)
        self.jacuzzi = jacuzzi  # Atributo adicional para definir si la habitación tiene jacuzzi


# Clase Cliente que gestiona la información del cliente y sus reservas
class Cliente:
    def __init__(self, nombre, correo):
        # Inicializa los atributos del cliente: nombre, correo y una lista para almacenar las reservas.
        self.nom = nombre  # Nombre del cliente
        self.correo = correo  # Correo electrónico del cliente
        self.reservas = []  # Lista para almacenar todas las reservas del cliente

    # Clase Reserva que crea una relación entre cliente, habitación y fechas


class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        # Inicializa una reserva con los datos del cliente, la habitación reservada y las fechas de inicio y fin.
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        # Se agrega la reserva al historial del cliente
        self.cliente.reservas.append(self)
        # La habitación se marca como no disponible
        self.habitacion.disponible = False  # Cambia el estado de disponibilidad de la habitación a 'no disponible'


# Función parser que extrae la información del documento de texto
def parser(documento): 
    flag = 0  # Indicador para saber cuándo se encuentra la línea del nombre del cliente
    with open(documento, 'r') as file:  # Abre el archivo para lectura
        for line in file:  # Recorre cada línea del archivo
            line = line.strip()  # Elimina los espacios en blanco al principio y al final de la línea
            lin = line.split()  # Separa la línea en una lista de palabras
            # Si la línea contiene palabras (no está vacía)
            if len(lin) > 0:
                # Si flag está activado, significa que hemos encontrado el nombre del cliente
                if flag == 1:
                    name = line.strip("-")  # Elimina el guión si está presente
                    clientx = Cliente(name, '-')  # Crea un nuevo cliente con el nombre extraído y un correo vacío
                    flag = 0  # Desactiva el indicador flag
                # Si la línea contiene la frase "Nombre del cliente", activa el indicador flag
                if "Nombre del cliente" in line: 
                    flag = 1
                # Si la línea contiene la palabra "correo", extrae el correo del cliente
                if "correo" in line:
                    print(lin)  # Muestra la lista de palabras en la línea (solo para depuración)
                    mail = lin[1]  # Asume que el correo está en la segunda palabra de la línea
                    clientx.correo = mail  # Asigna el correo al cliente
                    return clientx  # Devuelve el objeto cliente con su nombre y correo

# Llama a la función parser con el archivo de entrada
doc = str("INPUT.txt")
cliente = parser(doc)  # Se obtiene el cliente con su nombre y correo desde el archivo

# Imprime el nombre y el correo del cliente
print(cliente.nom)
print(cliente.correo)
