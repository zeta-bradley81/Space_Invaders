from tkinter import Tk
from turtle import Turtle, Screen

import aliens
import fighter
import weapons
from shelter import Shelter
from aliens import basicInvader
from time import sleep
import simpleaudio as simp
from playsound import playsound
from multiprocessing import Process

root = Tk()
root.withdraw()
monitor_height = root.winfo_screenheight()

game_height = int(monitor_height * .9)
game_width = int(game_height * 1.6)

BEAT_RATE = 0.07
CALIBRATION_VALUE = 20

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

i1 = basicInvader(SA, x_span, y_span, MARGIN, col_width, SIZE, row_height, row_0)
screen = Screen()
screen.setup(game_width, game_height)
screen.bgcolor('black')
screen.tracer(0)
i1.level_01()
screen.update()
screen.listen()

# wave_object = simp.WaveObject.from_wave_file("../Breakout/04-Book of Marseille.wav")
# # try to start thread to wait done while playing game. This is to know how/when to loop audio.
# wo = wave_object.play()
# # wo.wait_done()




f = fighter.Fighter(0, -y_span + 20, col_width, y_span)


screen.onkey(f.shoot, "Up")
screen.onkey(f.move_left, "Left")
screen.onkey(f.move_right, "Right")

shelter_area = game_width // 5
s1 = Shelter(4, 2, -x_span + shelter_area - 20, -y_span + 100, 'gray', 'red')
s1.create_shelter()
s2 = Shelter(4, 2, shelter_area * 2 - x_span - 20, -y_span + 100, 'gray', 'red')
s2.create_shelter()
s3 = Shelter(4, 2, shelter_area * 3 - x_span -20, -y_span + 100, 'gray', 'red')
s3.create_shelter()
s4 = Shelter(4, 2, shelter_area * 4 - x_span -20, -y_span + 100, 'gray', 'red')
s4.create_shelter()

game = True
state = game
beat = 0
l1 = aliens.Laser(50, 75)
l2 = aliens.Laser(60, 70)
l3 = aliens.Laser(70, 80)
laser_array = [l1, l2, l3]
while game:
    for n in range(len(i1.alien_invaders)):
        try:
            if f.mis.xcor() - CALIBRATION_VALUE < i1.alien_invaders[n].xcor() < f.mis.xcor() + CALIBRATION_VALUE:
                if f.mis.ycor() - CALIBRATION_VALUE < i1.alien_invaders[n].ycor() < f.mis.ycor() + CALIBRATION_VALUE:
                    i1.alien_invaders[n].hideturtle()
                    i1.alien_invaders.remove(i1.alien_invaders[n])
                    f.mis.goto(6000, 6000)
        except IndexError:
            pass
        # try:
        #     if l1.las.xcor() - CALIBRATION_VALUE < i1.alien_invaders[n].xcor() < l1.las.xcor() + CALIBRATION_VALUE:
        #         if l1.las.ycor() - CALIBRATION_VALUE < i1.alien_invaders[n].ycor() < l1.las.ycor() + CALIBRATION_VALUE:
        #             i1.alien_invaders[n].hideturtle()
        #             i1.alien_invaders.remove(i1.alien_invaders[n])
        # except IndexError:
        #     pass
        # if laser_array[0].color('yellow'):
        #     l1.las.color("blue")
        # else:
        #     l1.las.color("yellow")


    screen.update()

    # Basic Alien Motion and Soundtrack
    if beat % 8 == 0:
        state = i1.alien_motion()
    l1.laser_shoot()
    sleep(BEAT_RATE)

    if beat % 32 == 0:
        playsound("audio/01_alien_beat.wav", False)

    if f.weapons_status == False:
        f.missile_flight()

    beat += 1

    # Game Over
    if state == False:
        playsound("audio/06_loss_of_life.wav", False)
        sleep(.3)
        playsound("audio/07_alien_laugh.wav", False)
        game = False

screen.exitonclick()
