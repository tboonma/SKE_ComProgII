import turtle
turtle.speed(0)

def draw_triangle(size, n=3):
    if n == 0:
        return
    turtle.forward(size)
    turtle.left(120)
    draw_triangle(size, n-1)

def sierpinski(n, size=200):
    if n==0:
        draw_triangle(size)
    else:
        sierpinski(n-1, size/2)
        turtle.forward(size/2)
        sierpinski(n-1, size/2)
        turtle.left(60)
        turtle.forward(size/2)
        turtle.left(120)
        turtle.forward(size/2)
        turtle.left(180)
        sierpinski(n-1, size/2)
        turtle.right(120)
        turtle.forward(size/2)
        turtle.left(120)

sierpinski(5)
turtle.done()