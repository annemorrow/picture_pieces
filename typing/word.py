import pygame



class WordToType:

    def __init__(self, word):
        self.word = word
        self.done = 0
        self.word_font = pygame.font.SysFont("chalkduster.tff", 100)
        self.done_font = pygame.font.SysFont("chalkduster.tff", 120)

    def display(self, screen):
        if self.word == "NONE":
            return
        word = self.word_font.render(self.word, True, (0, 0, 0))
        done = self.done_font.render(self.word[:self.done], True, (200, 0, 250))
        screen.blit(word, (100, 400))
        screen.blit(done, (100, 100))

    def check_letter(self, letter):
        if letter == self.word[self.done]:
            self.done += 1

    def is_done(self):
        return self.done == len(self.word)
