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
            print("printing list")
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

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        else:
            temp.value = value
            return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            pre = self.get(index - 1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        while after:
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
print("element popped: ", my_linked_list.pop().value)
print("element popped: ", my_linked_list.pop())
my_linked_list.append(2)
print("element popped: ", my_linked_list.pop().value)
my_linked_list.prepend(19)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
my_linked_list.prepend(20)
my_linked_list.prepend(21)
print("element popped: ", my_linked_list.pop().value)
my_linked_list.print_list()
my_linked_list.pop_first()
my_linked_list.pop_first()
# print("printing")
my_linked_list.print_list()
print(my_linked_list.get(1).value)
my_linked_list.set_value(1, 60)
# print("printing")
my_linked_list.print_list()
my_linked_list.insert(1, 10)
my_linked_list.print_list()
my_linked_list.remove(1)
my_linked_list.remove(0)
my_linked_list.print_list()
my_linked_list.prepend(91)
my_linked_list.prepend(93)
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()
