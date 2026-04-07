class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def pop(self):
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return val

    def peek(self):
        return self.head.val

    def empty(self):
        return self.head is None

    def size(self):
        return self._size


class MyStack(object):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.push(x)

        while not self.q1.empty():
            self.q2.push(self.q1.pop())

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

    def pop(self):
        return self.q1.pop()

    def top(self):
        return self.q1.peek()

    def empty(self):
        return self.q1.empty()
