class Stack():

    def __init__(self):
        self.my_stack = []

    def push(self, el):
        self.my_stack.append(el)

    def pop(self):
        return self.my_stack.pop()

    def peek(self):
        return self.my_stack[-1]

    def is_empty(self):
        if len(self.my_stack) == 0:
            return True
        else:
            return False

