import pygame

class FisicaEntidades:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.tamanho = size
        self.velocidade = [0, 0]

    def atualizar(self, movimento=(0, 0)):
        frame_movimento = (movimento[0] + self.velocidade[0], movimento[1] + self.velocidade[1])

        self.pos[0] += frame_movimento[0]
        self.pos[1] += frame_movimento[1]

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)