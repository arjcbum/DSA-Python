class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            while temp.next:
                temp = temp.next
            temp2 = temp.prev
            temp2.next = None
            temp.prev = None
            self.tail = temp2
        self.length -= 1
        return temp


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop())

"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
