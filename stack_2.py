from test_data import TEST_1, TEST_2, TEST_3, TEST_4, TEST_5, TEST_6

CLOSER = {'(': ')', '[': ']', '{': '}'}


class Stack():
    """
    Stack is an abstract class that realises a list of elements organized by LIFO.
    """

    def __init__(self, string: str):
        self.stack = []
        self.string = string
        print('Класс инициализирован со следующими входными данными:', self.string)
        #self.string_splitted = list(self.string)

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
        self.stack.pop(-1)
        return self.stack[-1]

    def peek(self):
        """ The function for getting last stack element """
        return self.stack[-1]

    def size(self):
        """ The function returning the quntity of elements (stack size) """
        return len(self.stack)

    def isBalanced(self):
        """ The function is matching closing character and that the parenthesis pairs are correctly nested. Works with: (), [], {} only """
        for letter in self.string:
            #print('letter:', letter)
            if letter in CLOSER: #adding element to stack if it is opening
                self.push(letter)
            else: #if element is closing
                if CLOSER.get(self.peek()) == letter: #check is it fit for last stack element
                    self.pop()
                else:
                    print('Последовательность начинается с закрывающей скобки! Обработка прекращается!')
        if self.isEmpty():
            print(f'Cтрока {self.string} сбалансирована')
        else:
            print(f'Cтрока {self.string} не сбалансирована')
        print('Состав стэка: ', self.stack)