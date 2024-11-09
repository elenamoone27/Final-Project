# Create black background with scattered stars
import pygame
import random
import math
 

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((2560, 1440))
pygame.display.set_caption("Twinkling Stars")
clock = pygame.time.Clock()

stars = []
for _ in range(300):
    x = random.randint(0, 2560)
    y = random.randint(0, 1440)
    opacity = random.randint(50, 255)
    phase = random.uniform(0, 2 * math.pi)
    twinkle_speed = random.uniform(0.05, 0.2)
    star_surface = pygame.Surface((4, 4), pygame.SRCALPHA)
    pygame.draw.circle(star_surface, (255, 255, 255, opacity), (2, 2), 2)
    stars.append([x, y, star_surface, opacity, phase, twinkle_speed])

# Define stars

def draw_stars():
    for star in stars:
        star[4] += star[5]  # Increment phase
        star[3] = int((math.sin(star[4]) + 1) * 102.5 + 102.5)  # Calculate opacity
        star[3] = max(0, min(255, star[3]))
        star[2].set_alpha(star[3])
        screen.blit(star[2], (star[0], star[1]))


def draw_ufo(x, y, screen):
    pygame.draw.ellipse(screen, (150, 150, 150), (x, y, 160, 60))
    pygame.draw.ellipse(screen, (100, 100, 250), (x + 40, y - 20, 80, 40))

def animate_ufo(x, y, speed, beam_height, screen):
    global beam_active
    x += speed
    draw_ufo(x, y, screen)
    if x > 800:
        beam_active = True
    if beam_active:
        pygame.draw.polygon(screen, (255, 255, 100), 
                            [(x + 80, y + 60), (x + 40, y + 60 + beam_height), 
                             (x + 120, y + 60 + beam_height)])
        beam_height += 5
    return x, beam_height


def main():

    ufo_x, ufo_y = -200, 300
    ufo_speed = 5
    global beam_active
    beam_active = False
    beam_height = 0


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_stars()

        ufo_x, beam_height = animate_ufo(ufo_x, ufo_y, ufo_speed, beam_height, screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()