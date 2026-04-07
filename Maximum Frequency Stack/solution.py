from collections import deque


class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxFreq = 0

    def push(self, val):
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        f = self.freq[val]
        if f > self.maxFreq:
            self.maxFreq = f
        if f not in self.group:
            self.group[f] = deque()
        self.group[f].append(val)

    def pop(self):
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return val
