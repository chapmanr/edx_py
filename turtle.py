from turtle import *

def Recursive_Koch(length, depth):
    if depth == 0:
        forward(length)
    else:
        Recursive_Koch(length, depth-1)
        right(60)
        Recursive_Koch(length, depth-1)
        Recursive_Koch(120)
        Recursive_Koch(length, depth-1)
        right(60)
        Recursive_Koch(length, depth-1)
# ----------


left(90)
backward(300)
Recursive_Koch(10, 6)
