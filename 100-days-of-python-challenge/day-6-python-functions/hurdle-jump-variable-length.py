def turnright():
    turn_left() # type: ignore
    turn_left() # type: ignore
    turn_left() # type: ignore

def jump():
    turn_left() # type: ignore
    move() # type: ignore
    turnright() # type: ignore
    move() # type: ignore
    turnright() # type: ignore
    move() # type: ignore
    turn_left() # type: ignore

while at_goal() == False: # type: ignore
    if front_is_clear() == True: # type: ignore
        move() # type: ignore
    else:
        jump() # type: ignore