
CLOSER = {'(': ')', '[': ']', '{': '}'}


class Stack():
    """
    Stack is an abstract class that realises a list of elements organized by LIFO.
    """

    def __init__(self, string: str):
        self.stack = []
        self.string = string
        print('Класс инициализирован со входными данными:', self.string)
        self.STOP = False #Boolean var for immediate stop if closing element is first coming or delayed stop if there are ignored elements

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
        result = False

        if self.string[0] not in CLOSER:
            print('ОШИБКА-последовательность начинается с закрывающей скобки!')
            self.STOP = True

        if len(self.string) % 2 != 0:
            print('ОШИБКА-проверка четности не пройдена!')
            self.STOP = True
        else:
            print('Проверка четности пройдена успешно, анализируем содержание данных')

        for letter in self.string:
            if not self.STOP and letter in CLOSER: #adding element to stack if it is opening
                self.push(letter)
            else: #if element is closing

                if CLOSER.get(self.peek()) == letter: #check is it fit for last stack element
                    self.pop()
                else:
                    self.STOP = True
                    break

        if not self.STOP and self.isEmpty():
            print(f'Сбалансировано: {self.string}')
            result = True
        else:
            print(f'Не сбалансировано: {self.string}')

        return result