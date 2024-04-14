from collections import deque

class FreqElement:
    def __init__(self, val):
        self.val = val
        self.count = 0
    
    def __repr__(self):
        return f'{self.val}'

class FreqStack:
    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        exist = None
        val_obj = FreqElement(val)
        for i in self.stack:
            if i.val == val_obj.val:
                exist = i
                break
        if exist:
            exist.count += 1
            val_obj.count = exist.count
            self.stack.append(val_obj)
        else:
            val_obj.count = 1
            self.stack.append(val_obj)

    def pop(self) -> int:
        if not self.stack:
            return None
        most_freq = None
        current_freq = 0
        for i in self.stack:
            if i.count >= current_freq:
                current_freq = i.count
                most_freq = i
        print(most_freq, current_freq)
        if most_freq:
            self.stack.remove(most_freq)
            for i in self.stack:
                if i.val == most_freq.val:
                    i.count -= 1
            return most_freq.val
        return None
