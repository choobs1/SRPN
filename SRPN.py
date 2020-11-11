"""
@Author: Aman
Note: Multiline strings are used in some places as comments and are not to be
confused with program functionality.
"""

#list used as a stack data structure for the calculator
stack = []

# re -> regex used for token separation, random -> used to generate a random int
import re
import random as ran


#The main function is responsible for the program running
def main():
    print("You can now start interacting with the SRPN calculator")
    user_input()


#The function is responsible for the calculations that happen
def process_command(op):

    #If the certain characters or 
    if op == "" or op == " " or op == "#" or op.isalpha() == True and op != "d" and op != "r" :
        return

    # Check for the operator, if found, do the operation on the top two numbers on the stack
    if op == "+":
        x = stack.pop()
        y = stack.pop()
        stack.append(x+y)
    elif op == "-":
        x = stack.pop()
        y = stack.pop()
        stack.append(-(x-y))
    elif op == "*":
        x = stack.pop()
        y = stack.pop()
        stack.append(x*y)
    elif op == "/":
        x = stack.pop()
        y = stack.pop()
        #If division by zero occurs, kill stack and alert user
        try:
            stack.append(1/(x / y))
        except ZeroDivisionError:
            print("Divide by 0.")     
    elif op == "^":
        x = stack.pop()
        y = stack.pop()
        stack.append(x**y)
    elif op == "%":
        x = stack.pop()
        y = stack.pop()
        srack.append(x % y)
    elif op == "=":
        print(stack[-1])

    #Specific characters which affect the calculator
        #r -> appends random int
        #d -> prints the numbers in the stack
    elif op == "r":
        stack.append(ran.randint(0,2147483648))
    elif op == "d":
        print_stack(stack)

    #if the token passed to the function is anything other than the defined values, append it to the stack
    else:
        stack.append(int(op))


#Function prints all the items in the stack
def print_stack(s):
    for i in s:
        print(i)

#Function takes in user input for the calculator
def user_input():
    
    #While loop that runs continuosly for the user input
    while True:

        """Functions used to check if the token_list and stack are working"""
        #print(token_list)
        #print(stack)

        """A token list is used to separate numbers and chars in the input and then input the tokens
        into the process_command() function"""
        token_list = []

        """Check the requirements to put the char in our token list:
            the if statement checks if we get multiple inputs and the else statement
            checks if the char is already present in the token list or not
            """
        in_char = input()
        if len(in_char) > 1:
            token_list.extend(re.split("([^0-9])",in_char))
        else:
            if in_char in token_list:
                return
            else:
                token_list.append(in_char)
        for token in token_list:
            #Try and catch block checks if operation is being done on a single number
            try:
                process_command(token)
            except IndexError:
               print("Stack Underflow.")

# Main function called to run the program
main()
