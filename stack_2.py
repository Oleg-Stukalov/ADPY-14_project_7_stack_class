from test_data import TEST_1, TEST_2, TEST_3, TEST_4, TEST_5, TEST_6

CLOSER = {'(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{'}

#print(PAIRS['{'])

class Stack():
    """
    Stack is an abstract class that realises a list of elements organized by LIFO. It works with balanced/unbalanced parentheses.
    Balanced parentheses mean that each opening character has a matching closing character and that the parenthesis pairs are correctly nested.
    """

    def __init__(self, string: str):
        self.stack = []
        self.string = string
        self.string_splitted = list(self.string)
        self.pop_counter = 0 # коэф удаление пар скобок
        #print('string_splitted: ', len(self.string_splitted), self.string_splitted)
        if len(self.stack) % 2 != 0:
            print('Переданные данные НЕ сбалансированы! Дальнейшая проверка проверка прекращается.')
        else:
            print('Проверка четности пройдена успешно, анализируем содержание данных')

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
        self.stack.pop(len(self.stack) - 1)
        self.pop_counter += 1
        return self.stack[len(self.stack) - 1]

    def peek(self):
        """ The function for getting last stack element """
        return self.stack[len(self.stack) - 1]

    def size(self):
        """ The function returning the quantity of elements (stack size) """
        return len(self.stack)

    def isBalanced(self):
        """ The function is matching closing character and that the parenthesis pairs are correctly nested. Works with: (), [], {} only """
        if self.isEmpty():
            self.push(self.string[0])
        else:
            pass
        for index in range(1, len(self.string)):
            #print('***', self.peek())
            #print('+++', CLOSER[self.peek()])
            #print('---', len(self.string), self.string[index])
            if CLOSER[self.peek()] == self.string[index]:
                try:
                    self.pop()
                except:
                    IndexError
            else:
                self.push(self.string[index])

        if self.isEmpty():
            print(f'Cтрока {self.string} сбалансирована')
        else:
            print(f'Cтрока {self.string} не сбалансирована')
        print('Состав стэка: ', self.stack)



        # for index, element in enumerate(self.string_splitted):
        #     print('***', self.size())
        #     if index == 0:
        #         self.stack.append(element)
        #     else:
        #         if element != CLOSER[self.stack[index - 1 - self.pop_counter]]:
        #             self.stack.append(element)
        #         else:
        #             self.stack.pop()
        #
        # print('Стэк: ', self.stack)



#     Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок. Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга. Сбалансированными последовательности будут следующие скобки:
#
#     (((([{}]))))
#     [([])((([[[]]])))]{()}
#     {{[()]}} Несбалансированными последовательности:
#     }{}
#     {{[(])]}}
#     [[{())}] Программа ожидаем на вход строку с скобками. На выход сообщение "Сбалансированно", если строка корректная и "Небалансированно", если строка составлена не верно.
