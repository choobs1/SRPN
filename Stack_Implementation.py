class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])",expr)
    stack = Stack()
    for token in token_list:
        print(stack.items)
        if token == "" or token == " ":
            continue
        if token == "=":
            continue
        if token == "+":
            sums = stack.pop() + stack.pop()
            stack.push(sums)
        elif token == "-":
            diff = -(stack.pop() - stack.pop())
            stack.push(diff)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        elif token == "/":
            div = 1/(stack.pop()/stack.pop())
            stack.push(div)
        else:
            stack.push(int(token))
    return stack.pop()


def stackcheck():
    s = Stack()
    print(s.push(56))
    print(s.items)
    print(s.push(46))
    print(s.items)
    print(s.pop())
    print(s.pop())

def main():
    while True:
        in_char = input("Enter the number you dipshit: ")
        print(eval_postfix(in_char))
        



