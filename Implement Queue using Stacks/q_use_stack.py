class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'Node{self.data, self.next}'

class Stack:
    def __init__(self):
        self.head = None

    def __str__(self):
        res = ''
        current = self.head
        while current:
            res += str(current.data)
            res += ', '
            current = current.next
        return f'[{res[:-2]}]'

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

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

class MyQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.temp_stack = Stack()

    def push(self, x: int) -> None:
        while not self.main_stack.empty():
            self.temp_stack.push(self.main_stack.pop())
        self.temp_stack.push(x)
        while not self.temp_stack.empty():
            self.main_stack.push(self.temp_stack.pop())

    def pop(self) -> int:
        return self.main_stack.pop()

    def peek(self) -> int:
        return self.main_stack.top()

    def empty(self) -> bool:
        return self.main_stack.empty()