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

for step in range(6):
    jump()