#!/usr/bin/env python

# an rpn calculator in python
# > 19 2.14 + 4.5 2 4.3 / - *
# [85.297441860465113]
# only supports two operands and then an operator

import operator

ops = { '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div
}

def eval_expression(tokens, stack):
    for token in tokens:
        if set(token).issubset(set("0123456789.")):
            stack.append(float(token))
        elif token in ops:
            if len(stack) < 2:
                raise ValueError('Must have at least two parameters to perform op')
            a = stack.pop()
            b = stack.pop()
            op = ops[token]
            stack.append(op(b,a))
        else:
            raise ValueError("WTF? %s" % token)
    return stack

if __name__ == '__main__':
    stack = []
    while True:
        expression = raw_input('> ')
        if expression in ['quit','q','exit']:
            exit()
        elif expression in ['clear','empty']:
            stack = []
            continue
        elif len(expression)==0:
            continue
        stack = eval_expression(expression.split(), stack)
        print stack
