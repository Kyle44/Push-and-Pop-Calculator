# File:        proj2.py
# Written by:  Kyle Fritz
# Date:        11/26/2013
# Lab Section: 10
# UMBC email:  fritzk1@umbc.edu
# Description: This program acts as a calculator that understands how a one
#  line equation should be solved using the order of operations
############### USE WITH PYTHON 3 ###########
# scl enable python33 bash


import stack

def printGreeting():
    print("This is a calculator that knows how to use the")
    print("order of operations.  It will solve any one line equation.")
    print("This was created by Kyle Fritz from Lab Section 10")

# input: All three of your stacks
# output: The new value that is formed
def getValues(valueStack, inputStack, opStack):
    stack.pop(inputStack)
    # This is the operation
    z = stack.pop(opStack)
    # This is the first value
    A = stack.pop(valueStack)
    A = float(A)
    # This is the second value
    B = stack.pop(valueStack)
    B = float(B)
    newValue = findValue(B, z, A)
    return newValue

# input: Two values and an operation
# output: The new value formed by these three
def findValue(B, z, A):
    # Give new value a definition if no correct operand is present
    newValue = "???"
    if z == "+":
        newValue = B + A
    elif z == "*":
        newValue = B * A
    elif z == "-":
        newValue = B - A
    elif z == "/":
        newValue = B / A
    elif z == "%":
        newValue = B % A
    elif z == "^":
        newValue = B ** A    
    return newValue

# input: The stacks with values and operations
# output: A boolean to make sure that the equation can be solved
def validateEquation(valueStack, opStack):
    validChar = "+-*/%^("
    topOp = stack.top(opStack)
    topValue = stack.top(valueStack)
    # Pop topValue
    stack.pop(valueStack)
    # This determines whether an equation can be solved or not
    if topOp in validChar:
        try:
            secValue = stack.top(valueStack)
            secValue = float(secValue)
            stack.push(valueStack, topValue)
            return True
        except ValueError:
            return False
    else:
        stack.push(valueStack, topValue)
        return True

# input: The equation list, and the two dictionaries for priority
# output: Either the final answer or an error
def stackPush(listEquation, inputPriority, stackPriority):
    valueStack = stack.stack()
    opStack = stack.stack()
    inputStack = stack.stack()
    stack.push(valueStack, "$")
    stack.push(opStack, "$")
    stack.push(inputStack, -1)
    # To count the number of elements in the equation list
    count = 0
    for i in listEquation:
        count += 1
        print("Looking at", i, "in the equation")
        if i in "123456789":
            stack.push(valueStack, i)
            print("Adding", i, "to valueStack")
        elif i in "+-*/%^(":
            # This solves the part of the equation before this, until the new
            #  input priority can be put in
            while inputPriority [i] <= stack.top(inputStack):
                print("STACK VALUE >= the new INPUT PRIORITY.", end = " ") 
                print("So pop and process, and recheck.")
                newValue = getValues(valueStack, inputStack, opStack)
                newValue = float(newValue)
                print("New answer being placed into the VALUE", end = " ")
                print("stack is: ", newValue)
                stack.push(valueStack, newValue)
            stack.push(opStack, i)
            print(i, "was just added to opStack")
            stack.push(inputStack, stackPriority [i])
            print(stackPriority [i], "was just added to inputStack")
        elif i == ")":
            print("Pop and process, found a )")
            while stack.top(opStack) != "(" and stack.top(opStack) != "$":
                newValue = getValues(valueStack, inputStack, opStack)
                newValue = float(newValue)
                print("New answer being placed into the VALUE", end = " ")
                print("stack is: ", newValue)
                stack.push(valueStack, newValue)
            # This makes sure that there is a '(' in the equation   
            if stack.top(opStack) == "$":
                print("ERROR: unable to solve equation")
                return
            else:
                stack.pop(opStack)
                stack.pop(inputStack)
        if len(listEquation) == count:
            boolean = False
            # This determines if the equation has been solved or not
            if stack.top(valueStack) == "$" and stack.top(opStack) == "$":
                try:
                    stack.push(valueStack, newValue)
                    boolean = True
                except UnboundLocalError:
                    print("ERROR: unable to solve equation")
                    return
            while boolean == False:
                print("END OF EQUATION, so pop and process until", end = " ")
                print("opStack is only a '$'")
                topValue = stack.top(valueStack)
                # Solves for errors
                if stack.top(valueStack) == "$" and stack.top(opStack) != "$":
                    print("ERROR: unable to solve equation")
                    return
                stack.pop(valueStack)
                topValue = float(topValue)
                if stack.top(valueStack) == "$" and stack.top(opStack) == "$":
                    print("The answer is ", topValue)
                    return
                stack.push(valueStack, topValue)
                bool2 = validateEquation(valueStack, opStack)
                if bool2 == False:
                    print("ERROR: unable to solve equation")
                    return
                newValue = getValues(valueStack, inputStack, opStack)
                # Catches this error
                if newValue == "???":
                    print("ERROR: unable to solve equation")
                    return
                newValue = float(newValue)
                print("New answer being placed into the VALUE", end = " ")
                print("stack is: ", newValue)
                if stack.top(valueStack) == "$" and stack.top(opStack) == "$":
                    stack.push(valueStack, newValue)
                    boolean = True
                else:
                    stack.push(valueStack, newValue)
    newValue = stack.pop(valueStack)
    print("The answer is ", float(newValue))

# input: None
# output: Dictionaries for input and stack priority
def priorityFunc():
    inputPriority = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 5, "(": 6}
    inputPriority ["$"] = -1
    stackPriority = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 4, "(": 0}
    return inputPriority, stackPriority

def main():
    printGreeting()
    equation = "$"
    validChar = "1234567890+-^*/%()"
    while equation.lower() != "quit":
        flag = True
        equation = input("Type in a one line equation or 'quit' to quit: ")
        listEquation = list(equation.split())
        if equation.lower() != "quit":
            for i in listEquation:
                if len(i) > 1 or i not in validChar:
                    flag = False
            # Validates whether the input is correct        
            if flag == False:
                print("That is not a valid equation. ")
            else:
                print("The equation(list) we are looking at is: ", end = "")
                print(listEquation)
                inputPriority, stackPriority = priorityFunc()
                stackPush(listEquation, inputPriority, stackPriority)
main()
