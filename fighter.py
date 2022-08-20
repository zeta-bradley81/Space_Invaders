from turtle import Turtle, register_shape
from playsound import playsound


class Fighter(Turtle):
    def __init__(self, starting_x, starting_y, col_width, y_span):
        super().__init__()
        self.hideturtle()
        register_shape("fighter_shape_1", ((0, -33), (-15, 0), (0, 33)))
        self.weapons_status = True
        self.yspan = y_span

        self.cw = col_width
        self.f1 = Turtle()
        self.f1.penup()
        self.f1.shape('fighter_shape_1')
        self.f1.color("yellow")
        self.f1.goto(starting_x, starting_y)

        self.f2 = Turtle()
        self.f2.penup()
        self.f2.shape('triangle')
        self.f2.shapesize(.75, 1.5)
        self.f2.setheading(90)
        self.f2.color('red')
        self.f2.goto(starting_x, starting_y + 7.5)

        register_shape("squig", ((0, 0), (2, 2), (0, 4), (2, 6)))
        self.mis = Turtle()
        self.mis.penup()
        self.mis.goto(6000, 6000)
        self.mis.shape("squig")
        self.mis.shapesize(4, 7)
        self.mis.setheading(105)
        self.mis.color('yellow')
        self.ys = y_span
        self.fire_speed = 10

    def move_left(self):
        self.f1.backward(.5 * self.cw)
        self.f2.goto(self.f2.xcor() - (.5 * self.cw), self.f2.ycor())

    def move_right(self):
        self.f1.forward(.5 * self.cw)
        self.f2.goto(self.f2.xcor() + (.5 * self.cw), self.f2.ycor())

    def shoot(self):
        if self.weapons_status == True:
            self.weapons_status = False
            playsound("audio/05_shuttle_fire.wav", False)
            self.mis.goto(self.f2.xcor(), self.f2.ycor() + 20)
            return self.weapons_status

    def missile_flight(self):
        if self.weapons_status == False:
            if self.mis.ycor() < self.ys + 40:
                self.mis.goto(self.mis.xcor(), self.mis.ycor() + self.fire_speed)
            else:
                self.mis.goto(6000, 6000)
                self.weapons_status = True
                return self.weapons_status





    # def missile_fire(self):
    #     if self.mis.ycor() < self.ys + 40:
    #         self.mis.forward(100)
    #     else:
    #         self.mis.goto(-200, -self.ys)
