import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Curso Python")

background = pygame.image.load("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cnnbrasil.com.br%2Fesportes%2Ffutebol%2Ffutebol-internacional%2Fcristiano-ronaldo-marca-gol-925-na-carreira-veja%2F&psig=AOvVaw03HJKCKASN0ILjNuEKEXr7&ust=1740768596165000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIDU68PC5IsDFQAAAAAdAAAAABAE")

clock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0, 0))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":