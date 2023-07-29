import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position


line = input().split()
LX = int(line[0])
LY = int(line[1])
TX = int(line[2])
TY = int(line[3])

while True:
    remainingTurns = int(input())

    if TY > LY:
        print("N", end="")
        TY -= 1
    elif TY < LY:
        print("S", end="")
        TY += 1

    if TX > LX:
        print("W", end="")
        TX -= 1
    elif TX < LX:
        print("E", end="")
        TX += 1

    print("")
