from test_data import TEST_1, TEST_2, TEST_3, TEST_4, TEST_5, TEST_6

CLOSE = {'(': ')', '[': ']', '{': '}'}

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
        print('string_splitted: ', len(self.string_splitted), self.string_splitted)
        if len(self.stack) % 2 != 0:
            print('Переданные данные НЕ сбалансированы! Дальнейшая проверка проверка прекращается.')
        else:
            print('Проверка четности пройдена успешно, анализируем содержание данных')

    def isEmpty(self):
        if len(self.stack) == 0:
            isEmpty = True
        else:
            isEmpty = False
        return isEmpty

    #     push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self):
        for index, element in enumerate(self.string_splitted):
            print(index, element)
            try:
                if index >0 and element != self.stack[index - 1]:
                    self.stack.append(element)
                else:
                    self.stack.append(element)
            except:
                pass
        print('Стэк: ', self.stack)
        return self.stack


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


# Стек - абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»). Чаще всего принцип работы стека сравнивают со стопкой тарелок: чтобы взять вторую сверху, нужно снять верхнюю. Или с магазином в огнестрельном оружии(стрельба начнётся с патрона, заряженного последним).
#
#     Необходимо реализовать класс Stack со следующими методами:
#
#     isEmpty - проверка стека на пустоту. Метод возвращает True или False.
#     push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
#     pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
#     peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
#     size - возвращает количество элементов в стеке.
#
#     Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок. Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга. Сбалансированными последовательности будут следующие скобки:
#
#     (((([{}]))))
#     [([])((([[[]]])))]{()}
#     {{[()]}} Несбалансированными последовательности:
#     }{}
#     {{[(])]}}
#     [[{())}] Программа ожидаем на вход строку с скобками. На выход сообщение "Сбалансированно", если строка корректная и "Небалансированно", если строка составлена не верно.
