class Node:
    def __init__(self, v, p = None, n = None):
        self.value = v
        self.prev = p
        self.next = n

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val): #метод поиска первого узла по его значению
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val): #метод поиска всех узлов по конкретному значению
        node = self.head
        s = []
        while node is not None:
            if node.value == val:
                s.append(node)
            node = node.next
        return s

    def delete(self, val, all=False): #метод удаления одного\нескольких узла\ов по значению
            node = old = nxt = self.head
            while node is not None:
                if node.value == val:
                    if node == self.head and node == self.tail and node.value == val: #если в списке один узел
                        self.head = self.tail = None
                        node = old = nxt = None
                        break
                    elif node == self.head: #если узел первый
                        self.head = node.next
                        self.head.prev = None
                        old = node = nxt = node.next
                    elif node == self.tail: #узел последний
                        self.tail = node.prev
                        self.tail.next = None
                        node.prev = None
                    else:
                        old.next = nxt
                        nxt.prev = old
                    if all == False:
                        return
                old = node
                node = nxt
                if nxt != None:
                    nxt = nxt.next

    def clean(self): #метод очистки всего содержимого
        self.__init__()

    def len(self): #метод вычисления длины списка
        node = self.head
        s = 0
        while node != None:
            s += 1
            node = node.next
        return s

    def insert(self, afterNode, newNode): #метод вставки узла после заданного узла
        if afterNode is None:
            if type(newNode) == int:
                newNode = Node(newNode)
            if self.head == self.tail == None: #пустой
                self.add_in_head(newNode)
            else:
                self.add_in_tail(newNode)
        else:
            if type(newNode) == int:
                newNode = Node(newNode)
            if type(afterNode) == int:
                afterNode = Node(afterNode)
            node = self.head
            while True:
                if node.value == afterNode.value:
                    newNode.next = node.next
                    node.next = newNode
                    newNode.prev = node
                    if newNode.next is None:
                        self.tail = newNode
                    else:
                        node.next.prev = newNode
                    break
                else:
                    node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            item.prev = None
            item.next = None
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
