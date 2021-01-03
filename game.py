import pygame
from pygame.locals import *
import random
from os import listdir

from image_progress import ProgressImage
from word import WordToType

pygame.init()

screen = pygame.display.set_mode([800, 500])
clock = pygame.time.Clock()

with open("words.txt") as f:
    words = [line.strip() for line in f.readlines()]
random.shuffle(words)
# words = ["kaylee", "climbed", "a", "tree", "kaylee", "makes", "her", "frosty"]

# Have the pictures each have a sentence associated with the picture and
# and make it so the sentence completes the picture.

image_files = ["images/" + f for f in listdir("images")]
random.shuffle(image_files)
image_index = 0
prog_img = ProgressImage(image_files[image_index], 3, left=400, top=50)

word_index = 0
word = WordToType(words[word_index])
progress = 0

# Run until the user asks to quit
running = True
while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            letter = pygame.key.name(event.key)
            word.check_letter(letter)
            if word.is_done():
                progress += 1
                word_index = (word_index + 1) % len(words)
                word = WordToType(words[word_index])

        if progress == len(prog_img):
            word = WordToType("NONE")

        if event.type == pygame.MOUSEBUTTONDOWN and progress == len(prog_img):
            image_index = (image_index + 1)  % len(image_files)
            prog_img = ProgressImage(image_files[image_index], 3, left=400, top=50)
            progress = 0
            word_index = (word_index + 1) % len(words)
            word = WordToType(words[word_index])

        screen.fill((255, 255, 255))
        word.display(screen)
        prog_img.display(screen, progress)


    pygame.display.flip()



pygame.quit()
