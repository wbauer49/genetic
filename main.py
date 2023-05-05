
import pygame
import time

import definitions
import rendering


creatures = [definitions.Creature(100, 50)]

renderer = rendering.Renderer()

pygame.init()
running = True
while running:
    start_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

    for creature in creatures:
        creature.choose_move()

    for creature in creatures:
        creature.apply_move()

    renderer.render(creatures)
    pygame.display.flip()

    time.sleep(0.01)
