class Stack():
    """
    Stack is an abstract class that realises a list of elements organized by LIFO.
    """

    def __init__(self, string: str):
        self.stack = []
        self.string = string
        self.string_splitted = list(self.string)


    def isEmpty(self):
        """ Boolean function that indicates empty status of stack """
        if len(self.stack) == 0:
            isEmpty = True
        else:
            isEmpty = False
        return isEmpty

    def push(self):
        """ The function for adding element to stack """
        self.stack.append()

    def pop(self):
        """ The function for deleting last element, returning previous element """
        self.stack.pop(len(self.stack) - 1)
        return self.stack[len(self.stack) - 1]

    def peek(self):
        """ The function for getting last stack element """
        return self.stack[len(self.stack) - 1]

    #     size - возвращает количество элементов в стеке.
    def size(self):
        """ The function returning the quntity of elements (stack size) """
        return len(self.stack)

