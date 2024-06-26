import pygame
import sys
from scripts.entities import FisicaEntidades
from scripts.utils import carregar_imagens

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('teste')
        self.tela = pygame.display.set_mode((800, 600))

        self.clock = pygame.time.Clock()

        self.movimento = [False, False]

        self.assets = {
            'player': carregar_imagens('entities/player.png')
        }

        self.player = FisicaEntidades(self, 'player', (50, 50), (8, 15))


    def run(self):
        while True:
            self.tela.fill((14, 219, 248))

            self.player.atualizar((self.movimento[1] - self.movimento[0], 0))
            self.player.render(self.tela)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movimento[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movimento[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movimento[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movimento[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()