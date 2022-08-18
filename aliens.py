from turtle import Turtle
from random import randint
# TODO See commented out code below for ideas for an intro graphic

class Laser(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.las = Turtle()
        self.las.penup()
        self.las.shape('square')
        self.las.shapesize(.2, 1)
        self.las.setheading(270)
        self.las.color('pink')
        self.las.goto(x, y)

    def laser_shoot(self):
        if self.las.ycor() > -200:
            self.las.forward(5)
        else:
            self.las.goto(self.las.xcor(), 400)

class basicInvader(Turtle):
    def __init__(self, shape, xs, ys, mar, cw, size, rh, r0):
        super().__init__()
        self.shape = shape
        self.x_span = xs
        self.y_span = ys
        self.margin = mar
        self.col_width = cw
        self.size = size
        self.row_height = rh
        self.alien_invaders = []
        # TODO I think i need to move this down to the function
        self.top_row = r0 + 1.5 * rh
        self.alien_invaders = []
        self.direction = "left"
        self.num_of_lasers = 0
        # self.l1 = Laser(50, 60)
        # self.l2 = Laser(60, 70)
        # self.l3 = Laser(70, 80)



    def level_01(self):
        this_row = self.top_row
        for y in range(0, 8):
            this_row -= self.row_height
            for x in range(0, 16):
                if 3 < x < 13:
                    na = Turtle()
                    na.penup()
                    na.shape(self.shape)
                    na.shapesize(1.5, 1.5)
                    na.color("white")
                    na.goto((-self.x_span + self.margin + (x * self.col_width) - self.size // 2), this_row)
                    self.alien_invaders.append(na)

    def alien_motion(self):
        # move down a row
        for n in range(len(self.alien_invaders)):
            if self.direction == "left":
                self.alien_invaders[n].backward(self.col_width/4)
                if self.alien_invaders[n].xcor() <= -self.x_span + self.margin:
                    for n in range(len(self.alien_invaders)):
                        self.alien_invaders[n].goto(self.alien_invaders[n].xcor(), self.alien_invaders[n].ycor() - self.row_height)
                    self.direction = 'right'
                    # TODO figure out this value
                    if self.alien_invaders[n].ycor() <= -self.y_span +50:
                        # TODO gameover
                        return False
                    break
            else:
                self.alien_invaders[n].forward(self.col_width/4)
                if self.alien_invaders[n].xcor() >= self.x_span - self.margin:
                    for n in range(len(self.alien_invaders)):
                        self.alien_invaders[n].goto(self.alien_invaders[n].xcor(), self.alien_invaders[n].ycor() - self.row_height)
                    self.direction = 'left'
                    if self.alien_invaders[n].ycor() <= -self.y_span + 50:
                        # TODO gameover
                        return False
                    break

    # def laser_shoot(self):
    #     if randint(0,2) == 0:
    #         print(self.l1.xcor())
    #         self.l1.forward(10)







# from turtle import Turtle, Screen
#
# screen = Screen()
# screen.setup(800, 1000)
# screen.bgcolor('black')
# screen.tracer(0)
#
#
# for x in range(0, 100):
#     nl = Turtle()
#     # nl.hideturtle()
#     nl.color('white')
#     nl.goto(10*x - 500, 500)
#
# for x in range(0, 100):
#     nl = Turtle()
#     # nl.hideturtle()
#     nl.color('white')
#     nl.goto(10*x - 500, -400)
#
# for x in range(0, 100):
#     nl = Turtle()
#     nl.hideturtle()
#     nl.color('white')
#     nl.goto(10*x - 500, -20)
#
# screen.update()
# screen.exitonclick()
