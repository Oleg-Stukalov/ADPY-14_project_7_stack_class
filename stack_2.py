from test_data import TEST_1, TEST_2, TEST_3, TEST_4, TEST_5, TEST_6

CLOSER = {'(': ')', '[': ']', '{': '}'}


class Stack():
    """
    Stack is an abstract class that realises a list of elements organized by LIFO.
    """

    def __init__(self, string: str):
        self.stack = []
        self.string = string
        print('Класс инициализирован со входными данными:', self.string)
        self.STOP = False #Boolean var for immediate stop if closing element is first coming
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
        if self.isEmpty():
            result = 'Stack is empty!'
        else:
            self.stack.pop()
            result = self.peek()
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

    def isBalanced(self):
        """ The function is matching closing character and that the parenthesis pairs are correctly nested. Works with: (), [], {} only """
        if self.string[0] not in CLOSER:
            print('ВНИМАНИЕ ошибка! - последовательность начинается с закрывающей скобки!')
            self.STOP = True
            result = False
        for letter in self.string:
            #print('letter:', letter)
            if letter in CLOSER: #adding element to stack if it is opening
                self.push(letter)
            else: #if element is closing
                #print('!!!!!', CLOSER.get(self.peek()))
                if CLOSER.get(self.peek()) == letter: #check is it fit for last stack element
                    self.pop()
                # else:
                #     print('ВНИМАНИЕ ошибка! - последовательность начинается с закрывающей скобки!')
                #     self.STOP = True

        if not self.STOP:
            print('Длина и содержание стэка по результатам анализа: ', self.size(), self.stack)
            result = True

        if not self.STOP and self.isEmpty():
            print(f'Сбалансировано: {self.string}')
            result = True
        else:
            print(f'Не сбалансировано: {self.string}')

        return result