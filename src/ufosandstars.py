# Create black background with scattered stars
import turtle
import pygame

def main():

    print("main function")

def create_twinkling_stars():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
    pygame.quit()





if __name__ == "__main__":
    main()