import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.
# game loop


while True:
    l=0
    mi=0
    for i in range(8):
        mountain_h = int(input())  
        if  l <  mountain_h :
            l = mountain_h
            mi=i
    print( mi )


