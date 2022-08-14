from turtle import Turtle, register_shape


class Fighter(Turtle):
    def __init__(self, starting_x, starting_y):
        super().__init__()
        self.hideturtle()
        register_shape("fighter_shape_1", ((0, -33), (-15, 0), (0, 33)))
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
