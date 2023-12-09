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

    def print_list(self):
        temp = self.head
        if temp is None:
            print("LinkedList is empty")
        else:
            for _ in range(self.length):
                print(temp.value)
                temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        temp = self.head
        pre = self.head
        if temp is None:
            return None
        else:
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp


my_linked_list = LinkedList(1)
print("element popped: ", my_linked_list.pop().value)
print("element popped: ", my_linked_list.pop())
my_linked_list.append(2)
print("element popped: ", my_linked_list.pop().value)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()

print("element popped: ", my_linked_list.pop().value)
my_linked_list.print_list()
