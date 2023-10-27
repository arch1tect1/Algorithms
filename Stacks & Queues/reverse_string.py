class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def reverse_string(string):
    stack = Stack()
    reverse_string = ""
    
    for char in string:
        stack.push(char)
  
    while not stack.is_empty():
        reverse_string += stack.pop()
    return reverse_string
    
    # return string[::-1] # solution without using stack and its methods

my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
