# Create black background with scattered stars
import pygame
import turtle
import random
 

def setup_screen():
    turtle.tracer(0)
    global screen   
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)


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


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    stars = []
    for _ in range(100):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        opacity = random.randint(50, 255)
        stars.append([x, y, opacity])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        for star in stars:
            star[2] = (star[2] + random.randint(-10, 10)) % 256
            pygame.draw.circle(screen, (255, 255, 255, star[2]), (star[0], star[1]), 2)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()