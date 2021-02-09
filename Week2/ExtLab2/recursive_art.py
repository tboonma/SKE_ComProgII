import turtle
import random

""" Trying to draw earth.
    Submit many times because of THIS!!!!!
    I tried many art but I think this is so cute.
"""
turtle.bgcolor('black')
turtle.speed(0)     # To make the turtle be a turtle

def draw_land(land_type, n=5):
    def left(angle):
        turtle.left(angle)
    def right(angle):
        turtle.right(angle)
    turtle.pensize(55)
    if n == 0:
        return
    turn = random.choice([left, right])
    if land_type == 'green':
        if turtle.pos()[1] >= 150 and turtle.heading() >= 90:
            turn = left
        elif turtle.pos()[1] >= 150 and turtle.heading() <= 90:
            turn = right
        elif turtle.pos()[1] <= -150 and turtle.heading() >= 270:
            turn = left
        elif turtle.pos()[1] <= -150 and turtle.heading() <= 270:
            turn = right
    turn(40)
    turtle.forward(30)
    draw_land(land_type, n-1)
    turtle.backward(30)
    if turn == left:
        right(40)
    else:
        left(40)
    turtle.pensize(1)
    
def draw_circle(size, angle=360):
    if angle==0:
        return
    turtle.forward(size)
    turtle.left(1)
    draw_circle(size, angle-1)

def move_turtle(x_pos, y_pos):
    turtle.penup()
    turtle.goto(x_pos, y_pos)
    turtle.pendown()

def erase_outside_right(distance_list):
    if len(distance_list) == 0:
        return
    turtle.right(90)
    turtle.forward(distance_list.pop(0))
    erase_outside_right(distance_list)

def draw_all_land(n):
    if n == 0:
        return
    x = random.randint(-250, 250)
    y = random.randint(-330, 330)
    if y <= 280 and y >= 210:
        if abs(y-280) > abs(y-210):
            y = 280
        else:
            y = 210
    elif y >= -280 and y <= -210:
        if abs(y-280) > abs(y-210):
            y = 280
        else:
            y = 210
    move_turtle(x, y)
    if turtle.pos()[1] >= 230:
        turtle.pencolor('white')
        turtle.setheading(90)
        land_type = 'white'
    elif turtle.pos()[1] <= -230:
        turtle.pencolor('white')
        turtle.setheading(-90)
        land_type = 'white'
    else:
        turtle.pencolor('green')
        land_type = 'green'
        if turtle.pos()[1] <= -100:
            turtle.setheading(random.randint(70, 110))
        elif turtle.pos()[1] >= 100:
            turtle.setheading(random.randint(-110, -70))
        else:
            turtle.setheading(random.randint(0, 360))
    draw_land(land_type)
    draw_all_land(n-1)

move_turtle(0, -340)
turtle.pencolor('blue')
turtle.fillcolor('blue')
turtle.begin_fill()
draw_circle(6)
turtle.end_fill()
draw_all_land(30)
move_turtle(0, -340)
turtle.setheading(0)
turtle.pencolor('black')
turtle.fillcolor('black')
turtle.begin_fill()
draw_circle(6)
erase_outside_right([100, 400, 900, 900, 900, 500])
turtle.end_fill()
turtle.done()
