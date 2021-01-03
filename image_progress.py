from PIL import Image
import random
import pygame

class ImageSquare:
    def __init__(self, im, left, top):
        self.surf = pygame.image.fromstring(im.tobytes(), im.size, im.mode)
        self.left = left
        self.top = top
        self.width = self.surf.get_width()
        self.height = self.surf.get_height()

class ProgressImage:
    def __init__(self, img_path, div, left, top):
        self.left = left
        self.top = top
        self.squares = get_squares(img_path, div)
        max_sq = max(self.squares, key=lambda sq: (sq.left, sq.top))
        self.width = max_sq.left + max_sq.surf.get_width()
        self.height = max_sq.top + max_sq.surf.get_height()

    def __len__(self):
        return len(self.squares)

    def display(self, screen, progress):
        progress = min(progress, len(self.squares))
        pygame.draw.rect(screen, (0, 0, 0), (self.left - 1, self.top - 1,
                                             self.width + 2, self.height + 2))
        for sq in self.squares[:progress]:
            screen.blit(sq.surf, (self.left + sq.left, self.top + sq.top))
        for sq in self.squares[progress:]:
            pygame.draw.rect(screen, (210, 210, 210),
                (self.left + sq.left + 1, self.top + sq.top + 1,
                sq.width - 2, sq.height - 2))


def get_squares(img_path, div):
    img = Image.open(img_path)
    sqs = []
    width, height = img.size
    dx = width // div
    dy = height // div
    for x_count in range(width // dx):
        for y_count in range(height // dy):
            left = x_count * dx
            right = (x_count + 1) * dx
            top = y_count * dy
            bottom = (y_count + 1) * dy
            im = img.crop((left, top, right, bottom))
            sq = ImageSquare(im, left, top)
            sqs.append(sq)
    random.shuffle(sqs)
    return sqs
