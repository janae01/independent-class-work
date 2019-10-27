# Name: Janae Dorsey
# File: fallGreeting.py
#
# Purpose: This program will show an animated Thanksgivng Greeting Card

# Certification of Authenticity:
# I certify that this lab is entirely my own work.

from graphics import *
from time import sleep
import random


win = GraphWin("Halloween Greeting Card", 500, 500, autoflush=False)
win.setBackground(color_rgb(139,0,0))

#Circle for pumpkin
for i in range(100):
    radius = i
    p_circle = Circle(Point(250, 365), radius)
    p_circle.draw(win)
    p_circle.setWidth(3.5)
    p_circle.setFill(color_rgb(238,118,0))
    p_circle.setOutline(color_rgb(138, 54, 15))
    update(6.5)

#Stem of pumpkin
p_stem = Rectangle(Point(225, 220), Point(270, 268))
p_stem.setFill(color_rgb(138, 54, 15))
p_stem.setOutline(color_rgb(138, 54, 15))
p_stem.setWidth(3)
p_stem.draw(win)

#Eyes of pumpkin
p_reye = Circle(Point(220, 327), 10)
p_reye.setWidth(1.5)
p_reye.setOutline("saddlebrown")
p_leye = p_reye.clone()
p_leye.move(55, 0)
p_reye.draw(win)
p_leye.draw(win)

#Nose of pumpkin
p_nose = Polygon(Point(250,355), Point(225,385), Point(275,385))
p_nose.setWidth(1.5)
p_nose.setOutline("saddlebrown")
p_nose.draw(win)

#Mouth of pumpkin
p_mouth = Oval(Point(225, 413), Point(275, 428))
p_mouth.setOutline("saddlebrown")
p_mouth.setWidth(1.5)
p_mouth.draw(win)

#Holiday Message
holiday_msg = Text(Point(-160, 110), "Happy Halloween!")
holiday_msg.draw(win)
holiday_msg.setSize(30)
holiday_msg.setFace("times roman")
holiday_msg.setTextColor("gold")
holiday_msg.setStyle("bold")

#Loop for animations
time.sleep(0.5)
for i in range(175):
    r = random.randrange(256)
    b = random.randrange(256)
    g = random.randrange(256)
    color = color_rgb(r, g, b)
    p_reye.setFill(color)
    p_leye.setFill(color)
    p_nose.setFill(color)
    p_mouth.setFill(color)
    holiday_msg.move(5, 0)
    update(6.5)



#Exit instructions
exit_msg = Text(Point(250, 485), "Click anywhere to close.")
exit_msg.setFace("times roman")
exit_msg.setTextColor("white")
time.sleep(0.5)
exit_msg.draw(win)


win.getMouse()
time.sleep(0.5)
win.close()
