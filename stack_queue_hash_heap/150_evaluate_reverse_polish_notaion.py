def evalRPN(self, tokens: List[str]) -> int:

    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }

    stack = []
    for token in tokens:
        if token in operations:
            number_2 = stack.pop()
            number_1 = stack.pop()
            operation = operations[token]
            stack.append(operation(number_1, number_2))
        else:
            stack.append(int(token))
    return stack.pop()


def evalRPN1(self, tokens):

    stack = []

    for token in tokens:

        if token not in "+-/*":
            stack.append(int(token))
            continue

        number_2 = stack.pop()
        number_1 = stack.pop()

        result = 0
        if token == "+":
            result = number_1 + number_2
        elif token == "-":
            result = number_1 - number_2
        elif token == "*":
            result = number_1 * number_2
        else:
            result = int(number_1 / number_2)

        stack.append(result)

    return stack.pop()
