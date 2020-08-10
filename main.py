
import pygame

from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
color = (7, 49, 117)


clock = pygame.time.Clock()
def main():
	while True:
		clock.tick(60)
		screen.fill(color)
		pygame.display.flip()

main()