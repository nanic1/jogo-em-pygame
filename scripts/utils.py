import pygame
import os

BASE_IMG_PATH = 'data/images/'

def carregar_imagem(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def carregar_imagens(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(carregar_imagem(path + '/' + img_name))
    return images