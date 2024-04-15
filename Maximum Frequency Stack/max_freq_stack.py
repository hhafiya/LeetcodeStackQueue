from collections import deque

class FreqElement:
    def __init__(self, val):
        self.val = val
        self.count = 1
    
    def __repr__(self):
        return f'{self.val}'

class FreqStack:
    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        val_obj = FreqElement(val)
        for elem in self.stack:
            if elem.val == val:
                new_count = elem.count + 1
                val_obj.count += new_count
                break
        self.stack.appendleft(val_obj)

    def pop(self) -> int:
        current_freq = 0
        for elem in self.stack:
            if elem.count > current_freq:
                current_freq = elem.count
                most_freq = elem
        self.stack.remove(most_freq)
        return most_freq.val




