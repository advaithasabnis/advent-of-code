def infix_to_postfix(text, operators):
    """Uses shunting-yard algorithm to parse infix to postfix notation.
    Postfix notation is easy to evaluate and does not need parentheses.
    https://en.wikipedia.org/wiki/Shunting-yard_algorithm

    Parameters
    ----------
    text : str
        Input infix expression
    operators : dict
        Operator info including precedence precedence

    Returns
    -------
    str
        Postfix expression
    """
    infix = text.replace(" ", "")
    output = []
    stack = []
    for token in infix:
        if token.isdigit():
            output.append(int(token))
        elif token in operators:
            while (
                stack and stack[-1] != '(' and operators[stack[-1]].prec >= operators[token].prec
            ):
                # there is an operator o2
                # other than the left parenthesis at the top of the operator stack
                # and o2 has greater or equal precedence than o1
                # and o1 is left-associative
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            assert stack.pop() == '('
    while stack:
        assert stack[-1] != '('
        output.append(stack.pop())
    return output


def eval_infix(text, operators):
    """Converts infix to postfix and evaluates postfix

    Parameters
    ----------
    text : str
        Input infix string
    operators : dict
        Operator info including precedence precedence

    Returns
    -------
    int
        Value of evaluated expression
    """
    postfix = infix_to_postfix(text, operators)
    operands = []
    for token in postfix:
        if token in operators:
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = operators[token].calc(operand1, operand2)
            operands.append(result)
        else:
            operands.append(token)
    return operands.pop()
