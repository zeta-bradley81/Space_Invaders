from turtle import Turtle, register_shape


# class Laser(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.las = Turtle()
#         self.las.penup()
#         self.las.shape('square')
#         self.las.shapesize(.7, .2)
#         self.las.color('pink')
#         self.las.goto(100, 20)

# class Missile(Turtle):
#     def __init__(self, y_span):
#         super().__init__()
#         register_shape("squig", ((0,0), (2,2), (0,4), (2,6)))
#         self.mis = Turtle()
#         self.mis.penup()
#         self.mis.shape("squig")
#         self.mis.shapesize(4,7)
#         self.mis.setheading(105)
#         self.mis.color('yellow')
#         self.ys = y_span
#
#     def missile_fire(self):
#         if self.mis.ycor() < self.ys + 40:
#             self.mis.forward(100)
#         else:
#             self.mis.goto(-200, -self.ys)

