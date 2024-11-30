import pygame as pg
import sys

from pygame.time import Clock
from entities import PhysicsEntity
from util import load_image, load_images
from tilemap import Tilemap

clock = pg.time.Clock()


class Game:
    def __init__(self): # variables
        pg.init()
        self.screen = pg.display.set_mode((640, 480))
        self.movement = [False, False]

        self.assets = {'player' : load_image('entities/player.png'),
                      'background' : load_image('background.png'),
                      'grass' : load_images('tiles/grass'),
                      'stone' : load_images('tiles/stone'),
                      'large_decor' : load_images('tiles/large_decor')}

        self.tilemap = Tilemap(self)
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        self.display = pg.Surface((320, 240))
        self.frame = 60
        self.scroll = [0, 0]



    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0])
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1])

            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.tilemap.render(self.display, offset=render_scroll)
            self.player.render(self.display, offset=render_scroll)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = True
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pg.K_SPACE:
                        self.player.velocity[1] = -3
                    if event.key == pg.K_t:
                        self.frame = 2

                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = False
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pg.K_t:
                        self.frame = 2

                if event.type == pg.MOUSEBUTTONDOWN:
                    self.clickPos = (pg.mouse.get_pos()[0] // 2 + render_scroll[0], pg.mouse.get_pos()[1] // 2 + render_scroll[1])
                    self.tilemap.points.append(self.clickPos)
                    print(self.scroll)
                    print(self.clickPos)


            self.screen.blit(pg.transform.scale(self.display, (self.screen.get_size())), (0, 0))
            pg.display.update()
            clock.tick(self.frame)


Game().run()

