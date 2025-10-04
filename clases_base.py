import random

class Node:

  def __init__(self,value):
    self.__value = value
    self.__next = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self, node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("next debe ser none o un Nodo")
    self.__next = node

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self, newValue):
    if newValue is None:
      raise TypeError("Valor debe ser un objeto, no None")
    self.__value = newValue

class LinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  @head.setter
  def head(self, node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("head debe ser none o un Nodo")
    self.__head = node

  @tail.setter
  def tail(self, node):
   if node is not None and not isinstance(node,Node):
      raise TypeError("tail debe ser none o un Nodo")
   self.__tail = node

  def __iter__(self):
    curNode = self.__head
    while curNode is not None:
      yield curNode
      curNode = curNode.next

  def __str__(self):
    result = [str(node.value) for node in self]

    return ' --> '.join(result)


  def prepend(self, value):
    newNode = Node(value)
    if self.__head is None:
      self.__head = newNode
      self.__tail = newNode
    else:
      newNode.next = self.__head
      self.__head = newNode
    self.__size += 1

  def append(self, value):
    newNode = Node(value)
    if self.__head is None:
      self.__head = newNode
      self.__tail = newNode
    else:
      self.__tail.next = newNode
      self.tail = newNode
    self.__size += 1

  def getbyindex(self, index):
    if index <= 0 or index > self.__size:
      return "Error indice fuera rango"
    cont = 0


    current = self.__head
    while current is not None:
      cont += 1
      if cont == index:
        return current
      current = current.next

  def insertinindex(self, value, index):
    if index < -1 or index > self.__size:
      return "Error indice fuera rango"
    elif index == 0:
      self.prepend(value)
    elif index == -1:
      self.append(value)
    else:
      newNode = Node(value)
      prevNode = self.getbyindex(index-1)
      newNode.next = prevNode.next
      prevNode.next = newNode
      self.__size += 1

    return True

  def searchbyvalue(self, value):
    for node in self:
      if value == node.value:
        return True

    return False


  def popfirst(self):
    if self.__head is None:
      print("No hay elementos en la lista")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      popped_node = self.__head
      self.__head = self.__head.next
      self.__size -= 1
      popped_node.next = None
      return popped_node


  def pop(self):
    if self.__head is None:
      print("No hay elementos en la lista")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      popped_node = self.__tail
      new_tail = self.getbyindex(self.size-1)
      new_tail.next = None
      self.__tail = new_tail
      self.__size -= 1
      return popped_node

class NodeD:
  __slots__ = ('__value','__next', '__prev')

  def __init__(self,value):
    self.__value = value
    self.__next = None
    self.__prev = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = node

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue

  @property
  def prev(self):
    return self.__prev

  @prev.setter
  def prev(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("prev debe ser un objeto tipo nodo ó None")
    self.__prev = node


class DoublyLinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @head.setter
  def head(self, newHead):
    if newHead is not None and not isinstance(newHead,NodeD):
      raise TypeError("Head debe ser un objeto tipo nodo ó None")
    self.__head = newHead

  @property
  def tail(self):
    return self.__tail

  @tail.setter
  def tail(self, newTail):
    if newTail is not None and not isinstance(newTail,NodeD):
      raise TypeError("Tail debe ser un objeto tipo nodo ó None")
    self.__tail = newTail

  @property
  def size(self):
    return self.__size

  @size.setter
  def size(self, newSize):
    if not isinstance(newSize,int):
      raise TypeError("Size debe ser un objeto numero entero")
    self.__size = newSize

  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def print(self):
    for nodo in self:
      print(str(nodo.value))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def prepend(self, value):

    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      newnode.next = self.__head
      self.head.prev = newnode
      self.__head = newnode
    self.__size += 1

  def append(self,value):
    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode
      newnode.prev = self.__tail
      self.__tail = newnode

    self.__size += 1

  def getbyindex(self, index):
    if index < 0 or index > self.__size:
      return "Error, indice fuera de rango"

    cont = 0
    for currentNode in self:
      if cont == index:
        return currentNode
      cont += 1


  def insertinindex(self, value, index):

    if index == 0:
      self.prepend(value)
    elif index == -1 or index == self.__size:
      self.append(value)
    else:
      prevNode = self.getbyindex(index-1)
      nextNode = prevNode.next

      newNode = NodeD(value)
      newNode.next = prevNode.next
      prevNode.next = newNode
      newNode.prev = prevNode
      nextNode.prev = newNode
      self.__size +=1

      print("prev_new_node :",newNode.prev)
      print("prev_next_node :",nextNode.prev)

  def searchbyvalue(self, valuetosearch):
    for currentNode in self:
      if currentNode.value == valuetosearch:
        return True

    return False

  def setnewvalue(self, valuetochange, newvalue):
    for currentNode in self:
      if currentNode.value == valuetochange:
        currentNode.value = newvalue
        return True

    return False


  def pop(self):
    tempNode = self.__head
    if self.__head is None:
       print("Lista vacia, no hay elementos a eliminar")
       return None
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      poppednode = self.__tail
      prevnode = self.__tail.prev
      print("prevnode",prevnode)
      prevnode.next = None
      self.__tail = prevnode
      self.__size -= 1
      poppednode.prev = None
      return poppednode

  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return "Lista vacia, no hay elementos a eliminar"
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.head.prev = None
      self.__size -= 1

    tempNode.next = None
    return tempNode


  def generate(self, n, minvalue, maxvalue):
    for i in range(n):
      self.append(random.randint(minvalue, maxvalue))
    return self