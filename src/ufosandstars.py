# Create black background with scattered stars
import pygame
import turtle
import random
import math
 

def setup_screen():
    turtle.tracer(0)
    global screen   
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)


def draw_ellipse():
    turtle.penup()
    turtle.goto(-400, 0)  # Start off-screen
    turtle.pendown()
    turtle.fillcolor("grey")
    turtle.begin_fill()
    for angle in range(360):
        x = 267 * math.cos(math.radians(angle))
        y = 100 * math.sin(math.radians(angle))
        turtle.goto(x, y)
    turtle.end_fill()

def move_ellipse():
    for _ in range(80):
        turtle.forward(5)
        # Add a small delay if needed

# Set up screen
turtle.bgcolor("black")
# Draw stars here

# Draw and move ellipse
draw_ellipse()
move_ellipse()

turtle.done()

def draw_ellipse():
    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()
    turtle.fillcolor("grey")
    turtle.begin_fill()
    for _ in range(36):
        turtle.forward(20.47)
        turtle.left(360/36)
    turtle.end_fill()


def draw_stars():
    global stars
    for _ in range(150):
        star = turtle.Turtle()
        star.hideturtle()
        star.penup()
        star.color("white")
        star.goto(random.randint(-400, 400), random.randint(-300, 300))
        star.dot(random.randint(2, 5))
        stars.append(star)
        turtle.update()


def twinkle():
    global clock
    clock += 1
    if clock % 2 == 0:
        for star in stars:
            star.color("white" if random.random() > 0.5 else "gray")
    screen.ontimer(twinkle, 500)


draw_ellipse()
turtle.done()


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    stars = []
    for _ in range(100):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        opacity = random.randint(50, 255)
        phase = random.uniform(0, 2 * math.pi)
        twinkle_speed = random.uniform(0.05, 0.2)
        star_surface = pygame.Surface((4, 4), pygame.SRCALPHA)
        pygame.draw.circle(star_surface, (255, 255, 255, opacity), (2, 2), 2)
        stars.append([x, y, star_surface, opacity, phase, twinkle_speed])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        for star in stars:
            star[4] += star[5]  # Increment phase
            star[3] = int((math.sin(star[4]) + 1) * 102.5 + 102.5)  # Calculate opacity
            star[3] = max(0, min(255, star[3]))
            star[2].set_alpha(star[3])
            screen.blit(star[2], (star[0], star[1]))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()