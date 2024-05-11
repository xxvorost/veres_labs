class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.prev = None
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next
            if current.priority < priority:
                new_node.next = current
                new_node.prev = current.prev
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
            else:
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                new_node.prev = current

    def pop(self):
        if not self.head:
            raise IndexError("pop from empty priority queue")
        highest_priority_node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return highest_priority_node.value, highest_priority_node.priority

    def peek(self):
        if not self.head:
            raise IndexError("peek from empty priority queue")
        return self.head.value, self.head.priority
