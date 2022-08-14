import turtle
from turtle import Turtle, Screen

class Shelter(Turtle):
    def __init__(self, columns, rows, x_starting_pos, y_starting_pos, color='black', accent='red'):
        super().__init__()
        self.hideturtle()
        self.color = color
        self.accent = accent
        self.COLS = columns
        self.ROWS = rows
        self.X_START = x_starting_pos
        self.Y_START = y_starting_pos
        turtle.register_shape("right_tri", ((0, 10), (20, 10), (0, -10)))
        # 0 degrees = SouthEast triangle
        self.shelter_turtles = []

    def rt_shelter_block(self, orientation, x, y):
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.color(self.accent)
        new_turtle.penup()
        new_turtle.goto(x, y)
        new_turtle.shape("right_tri")
        new_turtle.setheading(orientation)
        new_turtle.showturtle()
        self.shelter_turtles.append(new_turtle)

    def sq_shelter_block(self, x, y):
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.color(self.color)
        new_turtle.penup()
        new_turtle.goto(x, y)
        new_turtle.shape("square")
        new_turtle.showturtle()
        self.shelter_turtles.append(new_turtle)

    def create_shelter(self):
        self.y_pos = self.Y_START
        self.x_pos = self.X_START
        for row in range(0, self.ROWS):
            for col in range (0, self.COLS):
                if row == 0:
                    if col == 0:
                        self.rt_shelter_block(270, self.x_pos, self.y_pos)
                        self.x_pos += 10

                    elif col == self.COLS - 1:
                        self.rt_shelter_block(180, self.x_pos, self.y_pos - 10)

                    else:
                        self.sq_shelter_block(self.x_pos, self.y_pos)
                        # new_turtle = Turtle()
                        # new_turtle.penup()
                        # new_turtle.goto(x_pos, y_pos)
                        # new_turtle.shape("square")
                        # shelter_turtles.append(new_turtle)
                        self.x_pos += 20
                else:
                    self.sq_shelter_block(self.x_pos, self.y_pos)
                    # new_turtle = Turtle()
                    # new_turtle.penup()
                    # new_turtle.goto(x_pos, y_pos)
                    # new_turtle.shape("square")
                    # shelter_turtles.append(new_turtle)
                    self.x_pos += 20
            self.y_pos -= 20
            self.x_pos = self.X_START - 10



screen = Screen()
screen.tracer(0)
screen.bgcolor('black')

s1 = Shelter(4, 2, -250, -200, 'gray', 'red')
s1.create_shelter()
s2 = Shelter(4, 2, -100,-200, 'gray', 'red')
s2.create_shelter()
s3 = Shelter(4, 2, 50,-200, 'gray', 'red')
s3.create_shelter()
s4 = Shelter(4, 2, 200,-200, 'gray', 'red')
s4.create_shelter()



screen.update()







#
# tri = Turtle()
# tri.shape('right_tri')
# tri.setheading(180)
# tri.shearfactor(.5)
# tri.setheading(90)
# tri.shapesize(1.,1.,2.)








screen.exitonclick()



