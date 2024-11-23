import pygame as pg

import tilemap


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0.0, 0.0]
        self.collisions = {'down' : False, 'up' : False, 'left': False, 'right' : False}

    def rect(self):
        return pg.Rect(self.pos[0], self.pos[1], *self.size)

    def update(self, movement = (0,0)):
        self.collisions = {'down': False, 'up': False, 'left': False, 'right': False}
        frame_movement = [movement[0] + self.velocity[0], movement[1] + self.velocity[1]]

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in self.game.tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['left'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['right'] = True

                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in self.game.tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True

                self.pos[1] = entity_rect.y

        self.velocity[1] = min(5.0, self.velocity[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
        if self.collisions['left'] or self.collisions['right']:
            self.velocity[0] = 0
    def render(self, screen, offset = (0, 0)):
        screen.blit(self.game.assets[self.type], (self.pos[0] - offset[0], self.pos[1] - offset[1]))


