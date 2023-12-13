class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedLists:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def print_ll(self):
        temp = self.head
        if temp:
            print("printing LL:")
            count = 0
            while temp:
                print(temp.value)
                temp = temp.next
                count += 1
            print("count: ", count)
        else:
            print("LL is empty!")

    def append(self, value):
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        temp1 = self.head
        temp2 = self.head
        while (temp2 is not None) and (temp2.next is not None):
            temp1 = temp1.next
            temp2 = temp2.next.next
        return temp1


my_linked_list = LinkedLists(1)
my_linked_list.print_ll()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.print_ll()

print(my_linked_list.find_middle_node().value)
