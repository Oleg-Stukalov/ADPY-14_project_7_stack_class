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

    def push(self, element):
        """ The function for adding element to stack """
        self.stack.append(element)

    def pop(self):
        """ The function for deleting last element, returning previous element """
        if self.isEmpty():
            result = 'Stack is empty!'
        else:
            self.stack.pop()
            result = self.peek()
            #self.stack.pop(len(self.stack) - 1)
        return result

    def peek(self):
        """ The function for getting last stack element """
        if self.isEmpty():
            result = 'Stack is empty!'
        else:
            result = self.stack[-1]
        return result

    def size(self):
        """ The function returning the quntity of elements (stack size) """
        return len(self.stack)

# string = '12345'
# stack000 = Stack(string)
# print('Push:', stack000.push(string[0]))
# print('Push:', stack000.push(string[1]))
# print('Stack:', stack000.stack)
# print('Size:', stack000.size())
# print('isEmpty:', stack000.isEmpty())
# print('Peek:', stack000.peek())
# print('Pop:', stack000.pop())
# print('Stack:', stack000.stack)