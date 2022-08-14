from turtle import Turtle
# TODO See commented out code below for ideas for an intro graphic

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
                self.alien_invaders[n].backward(1)
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
                self.alien_invaders[n].forward(1)
                if self.alien_invaders[n].xcor() >= self.x_span - self.margin:
                    for n in range(len(self.alien_invaders)):
                        self.alien_invaders[n].goto(self.alien_invaders[n].xcor(), self.alien_invaders[n].ycor() - self.row_height)
                    self.direction = 'left'
                    if self.alien_invaders[n].ycor() <= -self.y_span + 50:
                        # TODO gameover
                        return False
                    break








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
