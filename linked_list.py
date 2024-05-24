class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def insert(self, value, index):
        if index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def remove(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self):
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return ' -> '.join(result)


linked_list = LinkedList()
for i in range(10):
    linked_list.add(i)

linked_list.reverse()

print(linked_list)  # Expected output: 1 -> 2
