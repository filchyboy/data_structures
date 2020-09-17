# sketch 2

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("Index out of range")
            return None


