import pygame as pg

import tilemap


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0.0, 0.0]

    def rect(self):
        return pg.Rect(self.pos[0], self.pos[1], *self.size)

    def update(self, movement = (0,0)):
        frame_movement = [movement[0] + self.velocity[0], movement[1] + self.velocity[1]]

        entity_rect = self.rect()
        for rect in self.game.tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                pass



        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

        self.velocity[1] = min(5.0, self.velocity[1] + 0.1)

    def render(self, screen):
        screen.blit(self.game.assets[self.type], self.pos)


