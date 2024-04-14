import pygame
import pygame_gui
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, position, angle, x_scale, y_scale, xmin, ymin):
        super().__init__()

        image = pygame.image.load(image_path)

        self.image = pygame.transform.scale(image, (50, 33))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.position = position
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.xmin = xmin
        self.ymin = ymin
        x, y = self.scaled_pos
        print(y)
        self.rect.center = (x, y)

    @property
    def scaled_pos(self):
        scaled_x = self.x_scale * (self.position[0] - self.xmin)
        scaled_y = 600 - self.y_scale * (self.position[1] - self.ymin)

        return scaled_x, scaled_y

    def update(self, position, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        scaled_x, scaled_y = self.scaled_pos(position)
        self.rect.center = (scaled_x, scaled_y)