import pydirectinput

pydirectinput.PAUSE = 0
def forward():
    pydirectinput.keyUp('right',None,False)
    pydirectinput.keyUp('left',None,False)
    pydirectinput.keyUp('down',None,False)
    pydirectinput.keyDown('up',None,False)
    
    
def backward():
    pydirectinput.keyUp('right',None,False)
    pydirectinput.keyUp('left',None,False)
    pydirectinput.keyUp('up',None,False)
    pydirectinput.keyDown('down',None,False)
    
def right():
    pydirectinput.keyUp('up',None,False)
    pydirectinput.keyUp('left',None,False)
    pydirectinput.keyUp('down',None,False)
    pydirectinput.keyDown('right',None,False)
    
def left():
    pydirectinput.keyUp('up',None,False)
    pydirectinput.keyUp('right',None,False)
    pydirectinput.keyUp('down',None,False)
    pydirectinput.keyDown('left',None,False)
    
    
def nitro():
    pydirectinput.keyDown('space',None,False)
    pydirectinput.keyUp('space',None,False)