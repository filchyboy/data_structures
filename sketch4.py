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
        self.tail = None


    def add_to_head(self, value):
        new_node = Node(value)
        if self.head != None:
            new_node.set_next(self.head)
        self.head = new_node
    
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


    # def append(self, value):
    #     new_node = Node(value)
    #     while(self.head != None):
    #         while(self.tail != None):
    #             cur_node = self.tail
    #             while cur_node.next_node != None:
    #                 cur_node = cur_node.next_node
    #             cur_node.next_node = new_node
    #         else:
    #             cur_node = self.head
    #             while cur_node.next_node != None:
    #                 cur_node = cur_node.next_node
    #             cur_node.next_node = new_node
    #         return 

    def reverse(self):
        previous = None
        current = self.head 
        while(current != None): 
            next_node = current.next_node
            current.next_node = previous 
            previous = current 
            current = next_node
        self.head = previous 

    def add_to_tail(self, value):
        new_node = Node(value)
        while(self.tail != None):
            self.tail.set_next(new_node)
            self.tail = new_node


ll = LinkedList()

ll.add_to_head(1111)
print(ll.head.value)


ll.append(101)

# ll.append(102)

# ll.append(103)

# ll.append(104)

# ll.append(105)

print(ll.length())
print(ll.display())
# ll.delete_list()
ll.reverse()
print(ll.display())
ll.add_to_tail(111)
print(ll.display())
print(ll.tail)


