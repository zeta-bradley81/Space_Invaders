from turtle import Turtle

class scoreBoard():
    def __init__(self, x, y):
        super().__init__()
        self.scrbrd = Turtle()
        self.scrbrd.hideturtle()
        self.scrbrd.penup()
        self.scrbrd.color("green")
        self.scrbrd.goto(-x, y)
        self.scrbrd.write("00", align='left', font=("OCR A Std", 28, "bold"))

    def scoring(self, new_score):
        self.scrbrd.clear()
        self.scrbrd.write(new_score, align='left', font=("OCR A Std", 28, "bold"))

    def damage(self, new_damage):
        self.scrbrd.clear()
        self.scrbrd.write(new_damage, align='left', font=("OCR A Std", 28, "bold"))

