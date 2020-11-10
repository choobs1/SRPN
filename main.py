import random
#Initialising the 2 variables, x and y
num1 = 0 
num2 = 0
result = 0 
stack = []
#These are a list of operands which will be used throughout the code 
operator = ["+", "-", "/", "*", "^"]

#A function for the operation 
def Operation():
  result = 0 
  #A loop to remove the numbers and operators 
  for i in stack:
    operator = stack.pop()
    num2 = stack.pop()
    num1 = stack.pop()
    #If the operator in the quotation marks is present then do the operation
    if(operator == "+"):
      result = num1 + num2

    elif(operator == "-"):

      result = num1 - num2
  
    elif(operator == "*"):
      
      result = int(num1) * int(num2)

    elif(operator == "/"):
      #Using an if statement which states that
      #if the denominator is less than 0
      #then print the statment quoted below
      if num2 == 0:
        print ("dividing by 0")
      else: 
        result = num1/num2
    
    elif(operator == "^"):
      
      result = num1**num2
#Using if statements which states the maximum and
#minimum numbers
    if (result < -2147483648): 
      result = -21474836
    if (result > 2147483647):
      result = 2147483647 
#A function to add the result to the stack 
  stack.append(result) 
#This function checks whether the user input is an integer or not
def Num(userIn):
  try: 
    int(userIn)
    return True 
  except ValueError:
    return False 
#The eval function runs the code in brackets only
#when it's a string
def infix(queue):

  x = ["**" if element == "^" else element for  element in queue]

  str1 = ''.join(x)

  return (eval(str1))

def Checkinfix(userIn):
  for i in range(len(userIn)):
    if userIn[i] in operator:
      if i>1:
        return True
  return False 
#This is the main function which continuously runs 
while(True):
  userIn = input()
  #Used an if statement so that if "r" is entered
  #it recognises it as a random number
  if userIn == "r":
    stack.append(random.randint(0,2147483648))
  if Checkinfix(userIn):
    print(infix(userIn))
    
  if userIn == "=":
    #This prints the top value in the stack 
    print(stack[len(stack)-1])
  if Num(userIn):
    #This changes the string to an integer 
    userIn= int(userIn)
    stack.append(userIn)
  #This bit states that if the user input is in the operator then adds it to the stack 
  if userIn in operator:
    stack.append(userIn)
  #The code below checks the length of the stack
    if len(stack)<=2:
      print("Stack underflow")
    
    else:
          
#d displays what's in the stack 
#if d is entered then print it in the stack 
      Operation() 
  if userIn == "d":
    for i in stack:
      print (i)
#operations with single digits, only work when in decimal format
#e.g. 3.0+3.0 works fine 
