# Test the Stack

#from liststack import Stack
from lliststack import Stack

PROMPT = "Enter an int value (<0 to end): "
myStack = Stack()
value = int(input( PROMPT ))
while value >= 0:
    myStack.push( value )
    value = int(input( PROMPT ))

while not myStack.isEmpty():
    value = myStack.pop()
    print( value )
