class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node
        return new_node

    def remove_head(self):
        if self.head is None:
            return None
        else:
            ret_value = self.head.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
        return ret_value

    def remove_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def get_max(self):
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            return self.head.value
        current = self.head
        value = current.value
        while current.next is not None:
            if current.value > value:
                value = current.value
                current = current.next
            else:
                current = current.next
        if current.value > value:
            value = current.value
        return value 


sprocket = LinkedList()
sprocket.add_to_tail(2)
sprocket.add_to_tail(2)
sprocket.add_to_tail(2)

 

