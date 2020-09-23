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

# This function takes 1 argument and adds that value to the head of the
# linked list.

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.set_next(self.head)
        self.head = new_node

# This function takes no arguments and removes the head of the
# linked list.

    def remove_head(self):
        if self.head is None:
            return None
        else:
            ret_value = self.head.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next()
            return ret_value

# This function takes no arguments and deletes the linked list
# by decapitation.

    def delete_list(self):
        self.head = None

# This function takes no arguments and displays the contents of the
# linked list.

    def display(self):
        elements = []
        cur_node = self.head
        while self.head is not None:
            elements.append(self.head.value)
            while cur_node.next_node is not None:
                cur_node = cur_node.next_node
                elements.append(cur_node.value)
            return elements

# This function takes no arguments and returns the length of the
# linked list.

    def length(self):
        cur_node = self.head
        total = 0
        while cur_node.next_node is not None:
            total += 1
            cur_node = cur_node.next_node
        return total

# This function takes 1 argument and adds that value to the end of the
# linked list.

    def append(self, value):
        new_node = Node(value)
        cur_node = self.head
        while cur_node.next_node is not None:
            cur_node = cur_node.next_node
        cur_node.next_node = new_node

# This function takes no arguments and reverses the order of the
# linked list.

    def reverse(self):
        previous = None
        current = self.head
        while(current is not None):
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node
        self.head = previous

# This function takes no arguments and returns the maximum value
# in the linked list.

    def get_max(self):
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            return self.head.value
        current = self.head
        value = current.value
        while current.next_node is not None:
            if current.value > value:
                value = current.value
                current = current.next_node
            else:
                current = current.next_node
        if current.value > value:
            value = current.value
        return value


# This function takes 1 argument which is an index of the list.
# It returns the value of the data at that index.

    def get(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next_node
            if cur_index == index:
                return cur_node.value
            cur_index += 1

# This function takes 1 argument which is an index of the list.
# It deletes the value at that index.
# This is not yet working correctly.

    def delete_index(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        else:
            cur_index = 0
            cur_node = self.head
            while True:
                last_node = cur_node
                cur_node = cur_node.next_node
                if cur_index == index:
                    last_node.next = cur_node.next_node
                    if last_node.next_node is None:
                        self.tail = last_node
                    return
                cur_index += 1

# This function takes 1 argument. This adds the value to the tail of the list.
# This is not yet working correctly.

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            while(self.tail is not None):
                self.tail = new_node

# This function takes no arguments and deletes the tail of the linked list.

    def remove_tail(self):
        pass

#
# Interactions with classes
#

ll = LinkedList()
ll.add_to_head(101)
ll.append(102)
ll.append(0)
for i in range(1, 51):
    ll.append(i)
print("\nHead:",  ll.head.value)
print("\nLength:", ll.length())
print("\nMaximum Value:", ll.get_max())
print("\n", ll.display(), "\n\n")
# ll.delete_list()
ll.reverse()
print(ll.display())
# Add to tail not working
ll.add_to_tail(111)

# Append working
ll.append(111)
print("\n", ll.display(), "\n\n")
ll.delete_index(10)
print("\n", ll.display(), "\n\n")

print(ll.get(10))
ll.add_to_head(101)
print("\n", ll.display(), "\n\n")

# Remove_head is not working
ll.remove_head()
print("\n", ll.display(), "\n\n")

# Remove_head is not working
ll.remove_tail()
print("\n", ll.display(), "\n\n")
