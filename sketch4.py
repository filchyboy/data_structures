class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def delete(self):
        self.value = None
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None


    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)
        self.head = node

    def delete_list(self):
        self.head = None

    def display(self):
        elements = []
        cur_node = self.head
        while self.head is not None:
            while cur_node.next_node != None:
                cur_node = cur_node.next_node
                elements.append(cur_node.value)
            return elements

    def length(self):
        cur_node = self.head
        total = 0
        while cur_node.next_node != None:
            total += 1
            cur_node = cur_node.next_node
        return total

    def append(self, value):
        new_node = Node(value)
        cur_node = self.head
        while cur_node.next_node != None:
            cur_node = cur_node.next_node
        cur_node.next_node = new_node



ll = LinkedList()

ll.add_to_head(10)
print(ll.head.value)
ll.add_to_head(12)
print(ll.head.value)
ll.append(100)
ll.append(101)
ll.append(102)
ll.append(103)
ll.append(104)
ll.append(105)
print(ll.head.next_node.value)
print(ll.length())
print(ll.display())
ll.delete_list()
print(ll.display())


