class Stack():
    """
    Stack is an abstract class that realises a list of elements organized by LIFO. It works with balanced/unbalanced parentheses.
    Balanced parentheses mean that each opening character has a matching closing character and that the parenthesis pairs are correctly nested.
    """

    def __init__(self, string: str):
        self.stack = []
        self.string = string
        self.string_splitted = list(self.string)


    def isEmpty(self):
        if len(self.stack) == 0:
            isEmpty = True
        else:
            isEmpty = False
        return isEmpty

    #     push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self):
        self.stack.append()

    #     pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        self.stack.pop(len(self.stack) - 1)
        return self.stack[len(self.stack) - 1]

    #     peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return self.stack[len(self.stack) - 1]

    #     size - возвращает количество элементов в стеке.
    def size(self):
        return len(self.stack)

