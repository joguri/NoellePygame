import pygame

class Item:
    def __init__(self, filename):
        self.item = pygame.image.load(filename)
        self.rec = self.item.get_rect()
    
    def update(self, screen):
        screen.blit(self.item, self.rec)

class Character(Item):
    def __init__(self,filename):
        self.vSpeed = 0
        self.hSpeed = 0
        self.item = pygame.image.load(filename)
        self.rec = self.item.get_rect()
    def movex(self):
        self.rec.move_ip(self.hSpeed, 0)
    def movey(self):
        self.rec.move_ip(0, self.vSpeed)