# Filename: stack.py
# Contains the code to implement a Stack

# stack()
# creates a new stack
# Inputs: None
# Output: an empty stack
def stack():
    return[]

# top()
# returns the item on top of the stack without popping
# Inputs: items, a stack
# Output: an item from the stack, if not empty
def top(items):
    if isEmpty(items):
        return None
    else:
        return items[-1]

# isEmpty(items)
# checks to see if stack is empty
# Inputs: items, a stack
# Output: True if stack is empty, False if not
def isEmpty(items):
    return len(items) == 0

# push(items, item)
# pushes the item passed in onto the stack passed in, items.
# Inputs: items, a stack
#         item, an item to push onto the stack
# Output: None
def push(items, item):
    items.append(item)

# pop(items)
# pops an item from the stack passed in and returns it.
# Input: items, a stack
# Output: popped, the item popped from the stack or
#        "Empty Stack" if the stack was empty
def pop(items):
    size = len(items)
    if size > 0:
        popped = items[-1]
        del(items[-1])
        return popped
    else:
        return "Empty Stack"
