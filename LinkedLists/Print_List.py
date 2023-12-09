class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        if temp:
            for _ in range(self.length):
                print(temp.value)
                temp = temp.next
        else:
            print("LinkedList is empty!")


my_linked_list = LinkedList(4)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.empty()
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()
