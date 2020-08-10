

import pygame

from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
color = (13, 36, 115)


clock = pygame.time.Clock()

sprite_image = pygame.image.load("dimir praetor.jpg")
sprite_rect = sprite_image.get_rect()
sprite_image = pygame.transform.scale(sprite_image,(int(0.3*sprite_rect.width), int(0.3*sprite_rect.height)))
sprite_rect = sprite_image.get_rect()
sprite_rect.center = width // 2, height // 2


def main():
	while True:
		clock.tick(60)
		screen.fill(color)
		screen.blit(sprite_image, sprite_rect)
		pygame.display.flip()

main()