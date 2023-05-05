
import numpy as np
import pygame


WIDTH = 160
HEIGHT = 90
SIZE = 10


class Renderer:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH * SIZE, HEIGHT * SIZE))
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

    def render(self, creatures):
        self.screen.fill((255, 255, 255))
        for creature in creatures:
            self.render_creature(creature)

    def render_creature(self, creature):
        pygame.draw.rect(self.screen, (0, 0, 0), (creature.x * SIZE, (HEIGHT - creature.y) * SIZE, SIZE, SIZE))
        for i, appendage in enumerate(creature.appendages):
            x = creature.x + round(np.cos(np.radians(creature.angle + i * 90)))
            y = creature.y + round(np.sin(np.radians(creature.angle + i * 90)))
            pygame.draw.rect(self.screen, appendage.color, (x * SIZE, (HEIGHT - y) * SIZE, SIZE, SIZE))

