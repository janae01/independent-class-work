# Name: Janae Dorsey
# File: bumper.py
#
# Purpose: This program will create a simulation with two "cars" that change direction when they collide or when they
# hit a wall.
#
# Certification of Authenticity:
# I certify that this lab is entirely my own work.

from graphics import *
from random import randint
import math
from time import sleep

#returns a random integer in the range[-move_amount, +move_amont]
def get_random(move_amount):
    return randint(-move_amount, move_amount)

#returns boolean based on the collision of the two balls and changes color of balls upon collision
def did_collide(car1, car2):
    distance = math.sqrt((car2.getCenter().getX()-car1.getCenter().getX())**2 + (car2.getCenter().getY()-car1.getCenter().getY())**2)
    if distance <= sum([car1.getRadius(),car2.getRadius()]):
        random_color(car1)
        random_color(car2)
        return True
    else:
        return False

#returns boolean based on the ball hitting a vertical wall and changes color if so
def hit_vertical(car, width):
    if car.getCenter().getX() <= car.getRadius() or car.getCenter().getX() >= width - car.getRadius():
        random_color(car)
        return True
    else:
        return False

#returns boolean based on the ball hitting a horizontal wall and changes color if so
def hit_horizontal(car, height):
    if car.getCenter().getY() <= car.getRadius() or car.getCenter().getY() >= height - car.getRadius():
        random_color(car)
        return True
    else:
        return False

#returns a random color
def random_color(car):
        car.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        car.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))

def main():
    #assigns dimensions of windown
    width, height = 500, 500

    #creates window
    win = GraphWin("Joyride Bumper Cars", width, height)

    #draws first circle with random starting positon, color, and velocity
    car1 = Circle(Point(randint(35, 280), randint(35, 280)), 35)
    car1.draw(win)
    random_color(car1)
    x1_vel = get_random(15)
    y1_vel = get_random(15)

    #draws second circle with random starting position, color, and velocity
    car2 = Circle(Point(randint(35, 280), randint(35, 280)), 35)
    car2.draw(win)
    random_color(car2)
    x2_vel = get_random(20)
    y2_vel = get_random(20)

    #creates loop for the movement of the cars
    for i in range(1000):
        #moves cars
        sleep(.03)
        car1.move(x1_vel, y1_vel)
        car2.move(x2_vel, y2_vel)
        #tests if balls collides and changes their directions if so
        if did_collide(car1, car2):
            x1_vel = -(x1_vel)
            y1_vel = -(y1_vel)
            x2_vel = -(x2_vel)
            y2_vel = -(y2_vel)
        #tests if first ball hits horizontal wall and changes its direction if so
        if hit_horizontal(car1, width):
            y1_vel = -(y1_vel)
        #tests if second ball hits horizontal wall and changes its direction if so
        if hit_horizontal(car2, width):
           y2_vel = -(y2_vel)
        #tests if first ball hits vertical wall and changes its direction if so
        if hit_vertical(car1, height):
            x1_vel = -(x1_vel)
        #tests if second ball hits vertical wall and changes its direction if so
        if hit_vertical(car2, height):
            x2_vel = -(x2_vel)

main()



