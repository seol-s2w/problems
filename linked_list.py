class Node:
    def __init__(self, data):
        self.data = data
        self.prev: Node = None
        self.next: Node = None


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_back(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_front(self):
        if self.head is None:
            raise IndexError("pop from an empty LinkedList")

        data = self.head.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return data

    def pop_back(self):
        if self.tail is None:
            raise IndexError("pop from an empty LinkedList")

        data = self.tail.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return data

    def apply(self, func):
        results = []
        node = self.head
        while node is not None:
            results.append(func(node.data))
            node = node.next

        return results
