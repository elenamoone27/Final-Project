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
# Set up screen
turtle.bgcolor("black")
# Draw stars here
turtle.done()


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


def draw_ufo(x, y):
    pygame.draw.ellipse(screen, (150, 150, 150), (x, y, 80, 30))
    pygame.draw.ellipse(screen, (100, 100, 250), (x + 20, y - 10, 40, 20))

def animate_ufo(x, y, speed, beam_height):
    global beam_active
    x += speed
    draw_ufo(x, y)
    if x > 300:
        beam_active = True
    if beam_active:
        pygame.draw.polygon(screen, (255, 255, 100), 
                            [(x +40, y + 30)(x + 20, y + 30 + beam_height), 
                             (x + 60, y + 30 + beam_height)])
        beam_height += 5

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

    ufo_x, ufo_y = -100, 150
    ufo_speed = 3
    global beam_active
    beam_active = False
    beam_height = 0


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

        ufo_x, beam_height = animate_ufo(ufo_x, ufo_y, ufo_speed, beam_height)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()