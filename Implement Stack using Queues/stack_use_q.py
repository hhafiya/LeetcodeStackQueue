class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'Node{self.data, self.next}'

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        res = ''
        current = self.head
        while current:
            res += str(current.data)
            res += ', '
            current = current.next
        return f'[{res[:-2]}]'

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def pop(self):
        if self.size() == 1:
            popped = self.head.data
            self.head = None
            return popped
        elif self.empty():
            raise ValueError('Stack is empty')
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def empty(self):
        if self.head is None:
            return True
        return False

    def clear(self):
        self.head = None

    def top(self):
        if self.empty():
            raise ValueError("Stack is empty")
        return self.head.data

    def size(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count

class MyStack:
    def __init__(self):
        self.main_queue = Queue()
        self.temp_queue = Queue()

    def push(self, x: int) -> None:
        while not self.main_queue.empty():
            self.temp_queue.append(self.main_queue.pop())
        self.main_queue.append(x)
        while not self.temp_queue.empty():
            self.main_queue.append(self.temp_queue.pop())

    def pop(self) -> int:
        return self.main_queue.pop()

    def top(self) -> int:
        return self.main_queue.top()

    def empty(self) -> bool:
        return self.main_queue.empty()
