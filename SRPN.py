stack = []
import re


def main():
    print("You can now interact with the SRPN calculator")
    print()
    
    """while True:
        print(stack)
        token_list = []
        #print("Give input:")
        in_char = input()
        if len(in_char) > 1:
            token_list.extend(re.split("([^0-9])",in_char))
        else:
            if in_char in token_list:
                return
            else:
                token_list.append(in_char)
        print(token_list)
        for token in token_list:
            process_command(token)"""
    user_input()


def process_command(op):
    if op == "" or op == " ":
        return
    if len(stack) < 2 :
        print("Stack underflow.")
    """if op == "+":
        x = stack.pop()
        y = stack.pop()
        stack.append(x+y)
    elif op == "-":
        x = stack.pop()
        y = stack.pop()
        stack.append(x-y)
    elif op == "*":
        x = stack.pop()
        y = stack.pop()
        stack.append(x*y)
    elif op == "/":
        x = stack.pop()
        y = stack.pop()
        if y == 0:
            print("Divide by 0")
        else:
            stack.append(x/y)"""
    perform_operation(op)
    if op == "=":
        print(stack[-1])
    elif op == "d":
        print_stack(stack)
    else:
        stack.append(int(op))

def print_stack(s):
    for i in s:
        print(i)

def perform_operation(oper):
    if oper == "+":
        x = stack.pop()
        y = stack.pop()
        stack.append(x+y)
    elif oper == "-":
        x = stack.pop()
        y = stack.pop()
        stack.append(x-y)
    elif oper == "*":
        x = stack.pop()
        y = stack.pop()
        stack.append(x*y)
    elif oper == "/":
        x = stack.pop()
        y = stack.pop()
        if y == 0:
            print("Divide by 0")
        else:
            stack.append(x/y)

def user_input():
    while True:
        print(stack)
        token_list = []
        #print("Give input:")
        in_char = input()
        if len(in_char) > 1:
            token_list.extend(re.split("([^0-9])",in_char))
        else:
            if in_char in token_list:
                return
            else:
                token_list.append(in_char)
        print(token_list)
        for token in token_list:
            process_command(token)

main()
