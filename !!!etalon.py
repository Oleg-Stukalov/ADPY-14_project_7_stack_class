from stack import Stack


def check_balance(value_str):
    open_elements_list = ['[', '{', '(']
    closing_elements_list = [']', '}', ')']

    if value_str:
        stack = Stack()
        for char in value_str:
            if char in open_elements_list:
                stack.push(open_elements_list.index(char))
            elif char in closing_elements_list:
                if not stack.isEmpty and stack.peek() == closing_elements_list.index(
                        char):
                    stack.pop()
                else:
                    return print(f'Последовательность {value_str} - не верная')

        return print(f'Последовательность {value_str} - верная')

    return f'Строка пустая проверка баланса невозможна'