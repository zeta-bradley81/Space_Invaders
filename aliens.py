from turtle import Turtle, register_shape

class laser(Turtle):
    def __init__(self, x, y, ys):
        super().__init__()
        self.las = Turtle()
        self.las.penup()
        self.las.shape('square')
        self.las.shapesize(.2, 1)
        self.las.setheading(270)
        self.las.color('pink')
        self.las.goto(x, y)
        self.y_span = ys
        self.laser_status = False
        self.fire_speed = 7

    def laser_shoot(self):
        if self.las.ycor() < self.y_span:
            self.las.forward(self.fire_speed)
        else:
            pass

class basicInvader(Turtle):
    def __init__(self, xs, ys, mar, cw, size, rh, r0):
        super().__init__()
        for x in range(1, 10):
            register_shape(f'alien_gifs/alien_{x}.gif')
        # register_shape('alien_gifs/alien_1.gif')
        # register_shape('alien_gifs/alien_2.gif')
        # register_shape('alien_gifs/alien_3.gif')
        # register_shape('alien_gifs/alien_4.gif')
        # register_shape('alien_gifs/alien_5.gif')
        # register_shape('alien_gifs/alien_6.gif')
        # register_shape('alien_gifs/alien_7.gif')
        # register_shape('alien_gifs/alien_8.gif')
        # register_shape('alien_gifs/alien_9.gif')
        # register_shape("alien_gifs/alien_1_large.gif")
        self.x_span = xs
        self.y_span = ys
        self.margin = mar
        self.col_width = cw
        self.size = size
        self.row_height = rh
        self.alien_invaders = []
        self.top_row = r0 + 1.5 * rh
        self.alien_invaders = []
        self.direction = "left"
        self.num_of_lasers = 0


    def level_01(self):
        this_row = self.top_row
        for y in range(0, 8):
            this_row -= self.row_height
            for x in range(0, 16):
                if 3 < x < 13:
                    na = Turtle()
                    na.penup()
                    na.shape(f'alien_gifs/alien_{y+2}.gif')
                    # na.shape("alien_gifs/alien_{num}.gif".format(num=y))
                    # na.shapesize(1.5, 1.5)
                    na.goto((-self.x_span + self.margin + (x * self.col_width) - self.size // 2), this_row)
                    self.alien_invaders.append(na)


    def alien_motion(self):
        # self.alien_invaders[0].goto(self.alien_invaders[0].xcor(), self.alien_invaders[0].ycor() - 50)
        # move down a row
        for n in range(len(self.alien_invaders)):
            if self.direction == "left":
                self.alien_invaders[n].backward(self.col_width/4)
                if self.alien_invaders[n].xcor() <= -self.x_span + self.margin:
                    for n in range(len(self.alien_invaders)):
                        self.alien_invaders[n].goto(self.alien_invaders[n].xcor(), self.alien_invaders[n].ycor() - self.row_height)
                    self.direction = 'right'
                    # This ends the game
                    if self.alien_invaders[n].ycor() <= -self.y_span +50:
                        self.alien_invaders[n].goto(self.alien_invaders[n].xcor(), self.alien_invaders[n].ycor() - self.row_height)
                        # TODO gameover
                        return False
                    return 'shift'

            else:
                self.alien_invaders[n].forward(self.col_width/4)
                if self.alien_invaders[n].xcor() >= self.x_span - self.margin:
                    for n in range(len(self.alien_invaders)):
                        self.alien_invaders[n].goto(self.alien_invaders[n].xcor(), self.alien_invaders[n].ycor() - self.row_height)
                    self.direction = 'left'
                    # This ends the game
                    if self.alien_invaders[n].ycor() <= -self.y_span + 50:
                        # TODO gameover
                        return False
                    return "shift"

class bigAlien(Turtle):
    def __init__(self):
        super().__init__()
        register_shape("alien_gifs/alien_1_large.gif")

    def ba(self):
        big = Turtle()
        big.shape('alien_gifs/alien_1_large.gif')
        big.goto(0,0)

    # def level_02(self):
    #     na = Turtle()
    #     na.penup()
    #     na.shape("alien_gifs/alien_1_large.gif")
    #     na.goto(0,1000)
    #     self.alien_invaders.append(na)
