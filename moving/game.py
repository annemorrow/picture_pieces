import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

class Floater(pygame.sprite.Sprite):
    def __init__(self, image_path, colorkey=None):
        self.surf = pygame.image.load(image_path)
        if colorkey:
            self.surf.set_colorkey(colorkey)
        self.rect = self.surf.get_rect()
        self.pos = (300, 200)
        self.target_pos = (300, 200)
        self.speed = 2


    def display(self):
        left, top = self.pos
        width = self.rect.width
        height = self.rect.height
        screen.blit(self.surf, (left - width / 2, top - height / 2))

    def update(self):
        if self.target_pos == self.pos:
            return
        t_left, t_top = self.target_pos
        s_left, s_top = self.pos
        dist = ((t_left - s_left)**2 + (t_top - s_top)**2)**.5
        if dist <= self.speed:
            self.pos = self.target_pos
            return
        dx = (t_left - s_left) / dist * self.speed
        dy = (t_top - s_top) / dist * self.speed
        self.pos = (s_left + dx, s_top + dy)

ladybug = Floater("ladybug.png", (233, 233, 233))
owl = Floater("owl.png", (250, 250, 250))

main_character = ladybug
# Game loop.
while True:
  screen.fill((250, 250, 250))

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == MOUSEBUTTONDOWN:
        main_character.target_pos = event.pos

  # Update.
  main_character.update()

  # Draw.
  main_character.display()

  pygame.display.flip()
  fpsClock.tick(fps)
