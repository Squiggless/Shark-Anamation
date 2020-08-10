
import pygame

from pygame.locals import *

pygame.init()

screen_info = pygame.display.info()
size = (width, height) = (int(screen_info.current_w), int(screen_ info.current_h))
screen = pygame.display.set_mode(size)