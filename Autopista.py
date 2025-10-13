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


def accidente(autopista: DoublyLinkedList, placa_inicio, placa_final):
    actual = autopista.head

    while actual:
        if actual.value.placa == placa_inicio:
            accidentado1 = actual
        if actual.value.placa == placa_final:
            accidentado2 = actual
        actual = actual.next

    actual = accidentado1.next
    while actual and actual != accidentado2:
        actual.prev.next = actual.next
        actual.next.prev = actual.prev
        actual = actual.next

    accidentado1.prev.next = accidentado1.next
    accidentado1.next.prev = accidentado1.prev

    accidentado2.prev.next = accidentado2.next
    accidentado2.next.prev = accidentado2.prev

    print(accidentado1, accidentado2)
    return 
    

autopista = DoublyLinkedList()
vehiculos = (
    Vehiculo("ABC 123", "auto", 3),
    Vehiculo("ASH 543", "camion", 2),
    Vehiculo("HGF 789", "moto", 1),
    Vehiculo("EML 395", "moto", 1),
    Vehiculo("EKJ 527", "camion", 5),
    Vehiculo("ENS 245", "moto", 4),
    Vehiculo("NEW 347", "auto", 5),
    Vehiculo("NKE 893", "auto", 3)
)

for v in vehiculos:
    insertar_vehiculos(autopista, v)

print(autopista)
#ceder_paso(autopista)
#print(autopista)
accidente(autopista, "ASH 543", "EML 395")
print(autopista)