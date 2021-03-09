import turtle

def draw_square(size):
    '''Draw a square around its center whose size is determined by the input argument size
    '''
    turtle.penup()
    turtle.forward(size/2)
    turtle.left(90)
    turtle.forward(size/2)
    turtle.left(90)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(-size/2)
    turtle.right(90)
    turtle.forward(-size/2)

def recurse_draw_square(level, size, x, y):
    if level == 0:
        return
    
    turtle.penup()
    turtle.goto(x, y)
    draw_square(size)
    recurse_draw_square(level-1, size/2, x-size/2, y+size/2)
    recurse_draw_square(level-1, size/2, x+size/2, y+size/2)
    recurse_draw_square(level-1, size/2, x+size/2, y-size/2)
    recurse_draw_square(level-1, size/2, x-size/2, y-size/2)

turtle.speed(0)
turtle.setheading(0)
turtle.goto(0, 0)

recurse_draw_square(4, 200, 0, 0)
turtle.done()