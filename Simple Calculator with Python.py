# more of the calculator application

import simplegui


# intialize globals
store = 4
operand = 10


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    """ add contents of store and operand"""
    global store
    store = store + operand
    output()
    
def sub():
    """ subtract contents of store and operand"""
    global store
    store = store - operand
    output()
    
    
def mul():
    """ multiply contents of store and operand"""
    global store
    store = store * operand
    output()
    
def div():
    """ divide contents of store and operand"""
    global store, operand
    store = store / operand
    output()

def enter(inp):
    global operand
    operand = float(inp)
    output()
    

# create frame
f = simplegui.create_frame("Calculator",300,300)

# register event handlers
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add,100)
f.add_button("Sub", sub,100)
f.add_button("Mul", mul,100)
f.add_button("Div", div,100)
f.add_input("Enter operand", enter, 100)


# get frame rolling
f.start()
