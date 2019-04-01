class Node:
    def __init__(self, data = None):
        self.__data = data
        self.__previous = None
        self.__next = None


    def __del__(self):
        print(f"deleted data : [{self.__data}]")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, link):
        self.__previous = link

    @property
    def next(self):
        return self.next

    @next.setter
    def next(self, link):
        self.__next = link


class DoubleLinkedList:
    def __init__(self):
        # 더미의 생성시점은 DLL이 만들어 질때
        # head, tail, d_size
        self.head = Node()
        self.tail = Node()
        self.d_size = 0
        self.head.next = self.tail
        self.tail.previous = self.head

    # 리스트의 맨 앞에 데이터 추가
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        new_node.previous = self.head
        self.head.next.previous = new_node
        self.head.next = new_node
        

    def add_last(self, data):
        new_node = Node(data)
        new_node.next = self.tail
        new_node.previous = self.tail.previous
        self.tail.previous.next = new_node
        self.tail.previous = new_node

        
    def insert_after(self, data, node):
        new_node = Node(data)
        new_node.previous = node
        new_node.next = node.next
        node.next.previous = new_node
        node.next = new_node

    def insert_before(self, data, node):
        new_node = Node(data)
        new_node.next = node
        new_node.previous = node.previous
        node.previous.next = new_node
        node.previous = new_node


    