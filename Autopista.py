from clases_base import *

class Vehiculo:
    def __init__(self, placa: str, tipo: str, prioridad: int):
        self.placa = placa
        self.tipo = tipo
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.tipo} |{self.placa}| ({self.prioridad})"


def insertar_vehiculos(autopista: DoublyLinkedList, vehiculo):
    autopista.append(vehiculo)
    return

def ceder_paso(autopista: DoublyLinkedList):
    if not autopista.head:
        return
    
    cursor = autopista.head
    preferencial = 1

    while cursor:
        siguiente = cursor.next
        if cursor != autopista.head and cursor.value.tipo == "moto":

            if cursor.value.prioridad != preferencial:
                siguiente = cursor

            if cursor.prev:
                cursor.prev.next = cursor.next
            if cursor.next:
                cursor.next.prev = cursor.prev
            else:
                autopista.tail = cursor.prev

            cursor.prev = None
            cursor.next = autopista.head
            autopista.head.prev = cursor
            autopista.head = cursor
        cursor = siguiente
    
    return


Autopista = DoublyLinkedList()
vehiculos = (
    Vehiculo("ABC123", "auto", 3),
    Vehiculo("ASH543", "moto", 2),
    Vehiculo("HGF789", "moto", 1),
    Vehiculo("EML395", "moto", 1),
    Vehiculo("EKJ527", "camion", 5)
)

for v in vehiculos:
    insertar_vehiculos(Autopista, v)

print(Autopista)
ceder_paso(Autopista)
print(Autopista)