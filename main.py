

import pygame

from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
color = (13, 41, 133)


clock = pygame.time.Clock()

sprite_image = pygame.image.load("Shark.png")
sprite_rect = sprite_image.get_rect()

def main():
	while True:
		clock.tick(60)
		screen.fill(color)
		screen.blit(sprite_image, sprite_rect)
		pygame.display.flip()

main()