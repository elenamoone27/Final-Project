# Create black background with scattered stars
import pygame
import turtle
import random

def main():   
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)

    stars = []
    for _ in range(50):
        star = turtle.Turtle()
        star.hideturtle()
        star.penup()
        star.color("white")
        star.goto(random.randint(-400, 400), random.randint(-300, 300))
        star.dot(random.randint(2, 5))
        stars.append(star)


def twinkle():






if __name__ == "__main__":
    main()