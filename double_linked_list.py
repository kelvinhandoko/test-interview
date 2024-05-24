class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def __reversed__(self):
        current_node = self.tail
        while current_node:
            yield current_node
            current_node = current_node.prev

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data and current_node == self.head:
                if not current_node.next:
                    current_node = None
                    self.head = None
                    self.tail = None
                    return
                else:
                    next_node = current_node.next
                    next_node.prev = None
                    current_node.next = None
                    current_node = None
                    self.head = next_node
                    return
            elif current_node.data == data:
                if current_node.next:
                    next_node = current_node.next
                    prev_node = current_node.prev
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
                else:
                    prev_node = current_node.prev
                    prev_node.next = None
                    current_node.prev = None
                    current_node = None
                    self.tail = prev_node
                    return
            current_node = current_node.next

    def __str__(self):
        current_node = self.head
        result = []
        while current_node:
            result.append(str(current_node.value))
            current_node = current_node.next
        return '->'.join(result)

    def display_reverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev


double_linked_list = DoubleLinkList()
double_linked_list.append(1)
double_linked_list.append(2)
double_linked_list.append(3)
for node in reversed(double_linked_list):
    print(node, end='->')
print("None")  # For formatting the linked list presentation

print(double_linked_list)  # Expected output: 1->2
