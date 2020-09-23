# sketch 3

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
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
        return elements

    def print_elements(self):
        pass
        

    def get(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1


    def delete(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                if last_node.next == None:
                    self.tail = last_node
                return
            cur_index += 1

    def delete_tail(self):
        if self == None: 
            return None
        if self.next == None: 
            self = None
            return None
        second_last = self 
        while(second_last.next.next): 
            second_last = second_last.next
        second_last.next = None
        return self 

sprocket = Linked_List()
sprocket.append(2)
# sprocket.append(2)
# sprocket.append(2)
# sprocket.append(2)
# sprocket.append(12)
# sprocket.append(5)
# sprocket.append(4)
# sprocket.append(3)
print("Length", sprocket.length())
# print("Display", sprocket.display())
print(sprocket.get(1))
# sprocket.delete(5)
# print("Length", sprocket.length())
# print("Display", sprocket.display())
# print(sprocket.get(5))
# print(sprocket.delete_tail())


