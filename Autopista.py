from clases_base import *

class Vehiculo:
    def __init__(self, placa: str, tipo: str, prioridad: int):
        self.placa = placa
        self.tipo = tipo
        self.prioridad = prioridad

    def __str__(self):
        if self.tipo == "moto":
            rep = "🏍️"
        if self.tipo == "auto":
            rep = "🚙"
        if self.tipo == "camion":
            rep = "🚚"
        return f"{rep} |{self.placa}|({self.prioridad})"


def insertar_vehiculos(autopista: DoublyLinkedList, vehiculo):
    autopista.append(vehiculo)
    return

def ceder_paso(autopista: DoublyLinkedList):
    if not autopista.head:
        return
    
    cursor = autopista.head

    while cursor:
        siguiente = cursor.next
        if cursor != autopista.head and cursor.value.tipo == "moto" and cursor.value.prioridad == 1:

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

    print(f"💥 accidente entre los vehiculos {accidentado1} - {accidentado2} 💥")
    return 

def invertir_orden(autopista: DoublyLinkedList):
    actual = autopista.head
    cont_autos = 0
    cont_motos = 0

    while actual:
        if actual.value.tipo == "auto":
            cont_autos += 1
        if actual.value.tipo == "moto":
            cont_motos += 1
        actual = actual.next

    if cont_motos >= cont_autos:
        return "Hay mas motos que autos, no se invierte la vía"
    
    elif cont_motos < cont_autos:
        actual = autopista.head
        autopista.tail = autopista.head  # la antigua cabeza será la nueva cola
        nueva_cabeza = None

        while actual:
            siguiente = actual.next

            actual.next = actual.prev
            actual.prev = siguiente

            nueva_cabeza = actual

            actual = siguiente

        autopista.head = nueva_cabeza
        if autopista.head:
            autopista.head.prev = None
        if autopista.tail:
            autopista.tail.next = None
        
        print(f"nueva cola {autopista.tail}")
        print(f"nueva cabeza {autopista.head}")
    return
    

autopista = DoublyLinkedList()
vehiculos = (
    Vehiculo("ABC 123", "auto", 3),
    Vehiculo("ASH 543", "camion", 2),
    Vehiculo("EML 395", "moto", 1),
    Vehiculo("PKJ 527", "camion", 5),
    Vehiculo("ENS 245", "moto", 4),
    Vehiculo("HGF 789", "moto", 1),
    Vehiculo("NEW 347", "auto", 5),
    Vehiculo("NKE 893", "auto", 3)
)

for v in vehiculos:
    insertar_vehiculos(autopista, v)

print("\n---------------------- AUTOPISTA INICIAL ----------------------")
print(autopista)
print("\n----------- CEDER PASO A MOTOCICLISTAS CON PRIORIDAD -----------")
ceder_paso(autopista)
print(autopista)
print("\n-------------- 💥 ACCIDENTE ENTRE DOS VEHICULOS 💥 --------------")
accidente(autopista, "ASH 543", "ENS 245")
print(autopista)
print("\n------------------------ INVERTIR VIA ------------------------")
invertir_orden(autopista)
print(autopista)