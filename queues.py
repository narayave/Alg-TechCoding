
'''
	https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
'''

class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        return self.first[0]
        
    def pop(self):
        self.first = self.first[1:]
        self.second = self.second[:-1]
        
    def put(self, value):
        self.first = self.first + [value]
        self.second = [value] + self.second

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()

