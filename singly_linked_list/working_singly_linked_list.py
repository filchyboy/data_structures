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
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
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
        total = 1
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
        self.tail = new_node

# This function takes no arguments and reverses the order of the
# linked list.

    def reverse(self):
        previous = None
        current = self.head
        self.tail = self.head
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
        cur_index = 1
        cur_node = self.head
        while cur_node is not None:
            if cur_index == index:
                return cur_node.value
            cur_node = cur_node.next_node
            cur_index += 1


# This function takes 1 argument. This adds the value to the tail of the list.

    def add_to_tail(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

# This function takes no arguments and deletes the tail of the linked list.

    def remove_tail(self):
        cur_node = self.head
        while cur_node.next_node is not None:
            last_node = cur_node
            cur_node = cur_node.next_node
        last_node.next_node = None
        self.tail = last_node


# This function takes 1 argument which is an index of the list.
# It deletes the value at that index.

    def delete_index(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        else:
            cur_index = 1
            cur_node = self.head
            while cur_node.next_node is not None:
                last_node = cur_node
                cur_node = cur_node.next_node
                if cur_index == index -1:
                    last_node.next_node = cur_node.next_node
                    if last_node.next_node is None:
                        self.tail = last_node
                    return
                cur_index += 1


#
# Interactions with classes
#
# Instantiate linked list

ll = LinkedList()

# Add to head
print("\n\nAdding 101 to head .....")
ll.add_to_head(101)

# Recording keeping through count & display
print("Head:",  ll.head.value, "Length:", ll.length(), "Maximum Value:", ll.get_max(), "Tail:", ll.tail.value)
print("Complete list:", ll.display())

# Appending
print("\n\nAppending 102 to list .....")
ll.append(102)

# Recording keeping through count & display
print("Head:",  ll.head.value, "Length:", ll.length(), "Maximum Value:", ll.get_max(), "Tail:", ll.tail.value)
print("Complete list:", ll.display())

# Reversing the list
print("\n\nReversing list .....")
ll.reverse()

# Recording keeping through count & display
print("Head:",  ll.head.value, "Length:", ll.length(), "Maximum Value:", ll.get_max(), "Tail:", ll.tail.value)
print("Complete list:", ll.display())

# Adding a series through append
print("\n\nAdding a series through append .....")
for i in range(1, 11):
    ll.append(i)

# Recording keeping through count & display
print("Head:",  ll.head.value, "Length:", ll.length(), "Maximum Value:", ll.get_max(), "Tail:", ll.tail.value)
print("Complete list:", ll.display())

# Add to tail
print("\n\nAdding directly to tail .....")
ll.add_to_tail(111999)

# Recording keeping through count & display
print("Head:",  ll.head.value, "Length:", ll.length(), "Maximum Value:", ll.get_max(), "Tail:", ll.tail.value)
print("Complete list:", ll.display())

# Remove head
print("\n\nRemoving the head .....")
ll.remove_head()

# Recording keeping through count & display
print("Head:",  ll.head.value, "Length:", ll.length(), "Maximum Value:", ll.get_max(), "Tail:", ll.tail.value)
print("Complete list:", ll.display())

# Retrieve value from index
print("\n\nRetrieving value from index 2 .....")

# Recording keeping through count & display
print("Head:",  ll.head.value, "Length:", ll.length(), "Maximum Value:", ll.get_max(), "Retrieved Value:", ll.get(2), "Tail:", ll.tail.value)
print("Complete list:", ll.display())

# Delete value from index - not yet working
print("\n\nDeleting value from index 2 .....")
ll.delete_index(2)

# Recording keeping through count & display
print("Head:",  ll.head.value, "Length:", ll.length(), "Maximum Value:", ll.get_max(), "Retrieved Value:", ll.get(2), "Tail:", ll.tail.value)
print("Complete list:", ll.display())

# Remove the tail
print("\n\nRemove the tail .....")
ll.remove_tail()

# Recording keeping through count & display
print("Head:",  ll.head.value, "Length:", ll.length(), "Maximum Value:", ll.get_max(), "Retrieved Value:", ll.get(2), "Tail:", ll.tail.value)
print("Complete list:", ll.display())

# Deleting the list
print("\n\nDeleting the list .....")
ll.delete_list()

# Recording keeping through count & display
# print("Head:",  ll.head.value, "Length:", ll.length(), "Maximum Value:", ll.get_max(), "Retrieved Value:", ll.get(2), "Tail:", ll.tail.value)
print("Complete list:", ll.display())


