import pygame
import item

class Itemlist:
    
    def __init__(self):
        self.backgroundList = []
        self.characterList = []
        self.platformList = []
        self.enemyList = []
    
    def addBackground(self, obj):
        self.backgroundList.append(obj)
    
    def addCharacter(self, obj):
        self.characterList.append(obj)
    
    def addPlatform(self, obj):
        self.platformList.append(obj)
        
    def addEnemy(self, obj):
        self.enemyList.append(obj)
    
    def redraw(self, screen):
        for j in self.backgroundList:
            j.update(screen)
        for j in self.characterList:
            j.update(screen)
        for j in self.platformList:
            j.update(screen)
        for j in self.enemyList:
            j.update(screen)
        pygame.display.flip()