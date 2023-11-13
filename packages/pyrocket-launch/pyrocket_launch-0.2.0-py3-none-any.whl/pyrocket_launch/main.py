#!/bin/python3
from turtle import width

# Import library code
from p5 import *
from glfw.GLFW import *
from random import randint


# Setup global variables
screen_size = 400
rocket_y = screen_size

# The draw_rocket function goes here


# The draw_background function goes here


def setup():
    size(screen_size, screen_size)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image('planet.png')
    rocket = load_image('rocket.png')


def draw_rocket():
    global rocket_y  # Use the global rocket_y variable
    rocket_y -= 1  # Move the rocket
    image(rocket, 300/2, rocket_y, 64, 64)


def draw_background():
    background(0)  # Short for background(0, 0, 0) — black
    image(planet, 300/2, 300, 300, 300)  # Draw the image


def draw():
    draw_background()
    draw_rocket()


run()