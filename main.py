from turtle import Turtle, Screen, bgpic, register_shape
from tkinter import Tk

root = Tk()
root.withdraw()
monitor_height = root.winfo_screenheight()

game_height = int(monitor_height * .9)
game_width = int(game_height * 1.6)

# Shape of Alien
SA = 'square'
# Area of Outer Space
AOS = game_height * .8

row_height = AOS / 10
col_width = game_width // 17

MARGIN = col_width
SIZE = game_width // 25
x_span = game_width / 2
y_span = game_height / 2
row_0 = y_span - MARGIN
col_0 = -x_span + MARGIN
this_row = row_0 + row_height






screen = Screen()
screen.setup(game_width, game_height)
screen.bgcolor('black')
screen.tracer(0)
# screen.bgpic("/Users/atormey/Downloads/3aee3df5c7e413c08033f57fb09894edcf1def1b_00.gif")


alien_invaders = []
for y in range(0, 8):
    this_row -= row_height
    for x in range(0, 16):
        if 3 < x < 13:
            na = Turtle()
            na.penup()
            na.shape(SA)
            na.shapesize(1.5, 1.5)
            na.color("white")
            na.goto((-x_span + MARGIN + (x * col_width) - SIZE//2), this_row)




screen.update()
screen.listen()


screen.exitonclick()