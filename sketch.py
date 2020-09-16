class Node:
    def __init__(self, next_node):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node
    def add_to_tail(self, value):
        # 
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node
    def remove_head(self):
        if self.head is None:
            return None
        ret__value = self.head.get_value()
            elif self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
        return ret_value
        # TODO
    def remove_tail(self):
        # empty list    

        # list with 1 element

        # list with more than 1 element

        # TODO
    def contains(self, value):

        # loop through the ll until the next pointer is none
        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value() == value:
                return True
        return False
            # if we find 'value'
                # return true
        # return false
        # TODO time permitting
    def get_max(self):
        # TODO time permitting