# wave_object = simp.WaveObject.from_wave_file("../Breakout/04-Book of Marseille.wav")
# # try to start thread to wait done while playing game. This is to know how/when to loop audio.
# wo = wave_object.play()
# # wo.wait_done()

from tkinter import Tk
from turtle import Screen
from random import randint
import fighter
from shelter import Shelter
from aliens import basicInvader, laser
from time import sleep
import simpleaudio as simp
from playsound import playsound
from multiprocessing import Process

root = Tk()
root.withdraw()
monitor_height = root.winfo_screenheight()
game_height = int(monitor_height * .9)
game_width = int(game_height * 1.6)

# Tempo
BEAT_RATE = 0.07
# Adjusts for the size of the turtles
CALIBRATION_VALUE = 20
# Shape of Alien
SA = 'square'
FIRE_RATE = 3
active_lasers = 0

# Screen Measurements
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


def generate_shelters():
    shelter_area = game_width // 5
    s1 = Shelter(4, 2, -x_span + shelter_area - 20, -y_span + 100, 'gray', 'red')
    s1.create_shelter()
    shelter_list.append(s1)
    s2 = Shelter(4, 2, shelter_area * 2 - x_span - 20, -y_span + 100, 'gray', 'red')
    s2.create_shelter()
    shelter_list.append(s2)
    s3 = Shelter(4, 2, shelter_area * 3 - x_span - 20, -y_span + 100, 'gray', 'red')
    s3.create_shelter()
    shelter_list.append(s3)
    s4 = Shelter(4, 2, shelter_area * 4 - x_span - 20, -y_span + 100, 'gray', 'red')
    s4.create_shelter()
    shelter_list.append(s4)


def hit_an_alien():
    for n in range(len(i1.alien_invaders)):
        try:
            if f.mis.xcor() - CALIBRATION_VALUE < i1.alien_invaders[n].xcor() < f.mis.xcor() + CALIBRATION_VALUE:
                if f.mis.ycor() - CALIBRATION_VALUE < i1.alien_invaders[n].ycor() < f.mis.ycor() + CALIBRATION_VALUE:
                    playsound("audio/02_hit_alien.wav", False)
                    i1.alien_invaders[n].hideturtle()
                    i1.alien_invaders.remove(i1.alien_invaders[n])
                    f.mis.goto(6000, 6000)
        except IndexError:
            pass

def check_for_fire(input_laser):
    fire_sounds = ("audio/04A_alien_fire_01.wav", "audio/04B_alien_fire_02.wav", "audio/04C_alien_fire_03.wav")
    if randint(0, FIRE_RATE) == 0:
            a = randint(1, 8)
            input_laser.las.goto(i1.alien_invaders[-a].pos())
            s = randint(0,2)
            playsound(fire_sounds[s], False)
            input_laser.laser_status = True


def hit_by_laser():
    global active_lasers
    for n in range(len(laser_list)):
        if laser_list[n].laser_status == False:
            check_for_fire(laser_list[n])


        # If laser has missed
        if laser_list[n].las.ycor() < -y_span:
            laser_list[n].las.goto(laser_list[n].las.xcor(), 2000)
            laser_list[n].laser_status = False

        # Has laser hit the fighter?
        if laser_list[n].las.xcor() - 1.5 * CALIBRATION_VALUE <= f.f1.xcor() <= laser_list[n].las.xcor() + 1.5 * CALIBRATION_VALUE:
            if laser_list[n].las.ycor() - CALIBRATION_VALUE <= f.f1.ycor() <= laser_list[n].las.ycor() + CALIBRATION_VALUE:
                laser_list[n].laser_status = False
                laser_list[n].las.goto(laser_list[n].las.xcor(), 2000)
                playsound("audio/06_loss_of_life.wav", False)

        # Has laser hit a shelter?
        for sh in range(len(shelter_list)):
            for st in range(len(shelter_list[sh].shelter_turtles)):
                try:
                    if shelter_list[sh].shelter_turtles[st].xcor() - CALIBRATION_VALUE < laser_list[n].las.xcor() < shelter_list[sh].shelter_turtles[st].xcor() + CALIBRATION_VALUE:
                        if shelter_list[sh].shelter_turtles[st].ycor() - CALIBRATION_VALUE < laser_list[n].las.ycor() < shelter_list[sh].shelter_turtles[st].ycor() + CALIBRATION_VALUE:
                            playsound("audio/03_hit_shelter.wav", False)
                            shelter_list[sh].shelter_turtles[st].hideturtle()
                            shelter_list[sh].shelter_turtles.remove(shelter_list[sh].shelter_turtles[st])
                            laser_list[n].las.goto(1000, 1000)
                            laser_list[n].laser_status = False
                except IndexError:
                    pass


    #                     TODO lose a life



# def alien_attacks():
#     pass
#     global active_lasers
#     if randint(0, FIRE_RATE) == 0:
#         if active_lasers < len(laser_list):
#             a = randint(1, 8)
#             laser_list[active_lasers].las.goto(i1.alien_invaders[-a].pos())
#             active_lasers += 1
#             print("FIRE")
#     else:
#         pass

# ~~~~~~~~~~~~~~~~~    Initialize Graphics    ~~~~~~~~~~~~~~~~~
screen = Screen()
screen.setup(game_width, game_height)
screen.bgcolor('black')
screen.tracer(0)
# Aliens
i1 = basicInvader(SA, x_span, y_span, MARGIN, col_width, SIZE, row_height, row_0)
i1.level_01()
# Player
f = fighter.Fighter(0, -y_span + 20, col_width, y_span)

# Shelters


shelter_list = []
generate_shelters()
shelter_top = shelter_list[0].shelter_turtles[1].ycor() + CALIBRATION_VALUE


# Alien Lasers
# todo fix the initial values
laser_list = [laser(2000, 2000, y_span), laser(10000, 10000, y_span), laser(20000, 20000, y_span)]
screen.update()
screen.listen()

# ~~~~~~~~~~~~~~~~~   Key Controls ~~~~~~~~~~~~~~~~~
screen.onkey(f.shoot, "Up")
screen.onkey(f.shoot, "space")
screen.onkey(f.shoot, "s")
screen.onkey(f.move_left, "Left")
screen.onkey(f.move_left, "a")
screen.onkey(f.move_right, "Right")
screen.onkey(f.move_right, "d")

game = True
state = game
beat = 0
shelter_list[0].shelter_turtles[2].hideturtle()
shelter_list[0].shelter_turtles.remove(shelter_list[0].shelter_turtles[2])

while game:
    screen.update()
    if f.weapons_status == False:
        f.missile_flight()
    hit_an_alien()
    hit_by_laser()
    # alien_attacks()
    for i in range(len(laser_list)):
        laser_list[i].laser_shoot()
    if beat % 8 == 0:
        state = i1.alien_motion()
    if beat % 32 == 0:
        # print(laser_list[1].las.ycor(), laser_list[2].las.ycor(), laser_list[0].las.ycor(), active_lasers)
        playsound("audio/01_alien_beat.wav", False)
    sleep(BEAT_RATE)
    beat += 1

    # Game Over
    if state == False:
        playsound("audio/06_loss_of_life.wav", False)
        sleep(.3)
        playsound("audio/07_alien_laugh.wav", False)
        game = False

screen.exitonclick()
