def turnright():
    turn_left() # type: ignore
    turn_left() # type: ignore
    turn_left() # type: ignore

while front_is_clear() == True: # type: ignore
    move() # type: ignore
turn_left() # type: ignore

while at_goal() == False: # type: ignore
    if right_is_clear() == True: # type: ignore
        turnright() # type: ignore
        move() # type: ignore
    elif front_is_clear() == True: # type: ignore
        move() # type: ignore
    else:
        turn_left() # type: ignore