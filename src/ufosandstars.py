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


def draw_lights(x, y, screen, frame_count):
    positions = [(x + 20, y + 30), (x + 140, y + 30), (x + 80, y + 40)]
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    
    # Change colors based on frame count
    for i, pos in enumerate(positions):
        color = colors[(frame_count // 10 + i) % len(colors)]
        pygame.draw.circle(screen, color, pos, 5)


def draw_ufo(x, y, screen, frame_count):
    pygame.draw.ellipse(screen, (150, 150, 150), (x, y, 160, 60))
    pygame.draw.ellipse(screen, (100, 100, 250), (x + 40, y - 20, 80, 40))
    draw_lights(x, y, screen, frame_count)


def animate_ufo(x, y, speed, beam_height, screen, frame_count):
    global beam_active
    x += speed
    draw_ufo(x, y, screen, frame_count)
    if x > 800:
        beam_active = True
    if beam_active:
        if frame_count % 20 < 10:
            pygame.draw.polygon(screen, (255, 255, 100), 
                                [(x + 80, y + 60), (x + 30, y + 600 + beam_height), 
                                 (x + 130, y + 600 + beam_height)])
            beam_height += 5
    return x, beam_height


def display_text(screen, frame_count):
    font = pygame.font.Font(None, 150)
    text = font.render("Are we really alone?", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    alpha = min(255, (frame_count - 200) * 2) 
    text.set_alpha(alpha)
    screen.blit(text, text_rect)


def main():

    ufo_x, ufo_y = -200, 300
    ufo_speed = 5
    global beam_active
    beam_active = False
    beam_height = 0
    frame_count = 0


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_stars()
        
        if ufo_x <= 2560:
            ufo_x, beam_height = animate_ufo(ufo_x, ufo_y, ufo_speed, beam_height, screen, frame_count)
        else:
            display_text(screen, frame_count)

        pygame.display.flip()
        clock.tick(30)
        frame_count += 1

    pygame.quit()

if __name__ == "__main__":
    main()