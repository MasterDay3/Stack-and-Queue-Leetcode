class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.top is None:
            return None
        val = self.top.val
        self.top = self.top.next
        self._size -= 1
        return val

    def peek(self):
        if self.top is None:
            return None
        return self.top.val

    def empty(self):
        return self.top is None

    def size(self):
        return self._size


class MyQueue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def move(self):
        while not self.inStack.empty():
            self.outStack.push(self.inStack.pop())

    def push(self, x):
        self.inStack.push(x)

    def pop(self):
        if self.outStack.empty():
            self.move()
        return self.outStack.pop()

    def peek(self):
        if self.outStack.empty():
            self.move()
        return self.outStack.peek()

    def empty(self):
        return self.inStack.empty() and self.outStack.empty()
