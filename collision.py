import pygame
import item

def inAir(player, platforms):
    for j in platforms:
        if player.rec.bottom == j.rec.top:
            if player.rec.left < j.rec.right and player.rec.right > j.rec.left:
                return 0
    return 1


def snapHorizontal(player, platforms):
    for j in platforms:
        snapH(player, j)
    
def snapVertical(player, platforms):
    for j in platforms:
        snapV(player, j)  
    
def snapH(player, item):
    if player.rec.colliderect(item.rec):
        if player.rec.left < item.rec.right and player.rec.right > item.rec.right:
            player.rec.left = item.rec.right
        if player.rec.right > item.rec.left and player.rec.left < item.rec.left:
            player.rec.right = item.rec.left
    
def snapV(player, item):
    if player.rec.colliderect(item.rec):
        if player.rec.bottom > item.rec.top and player.rec.top < item.rec.top:
            player.rec.bottom = item.rec.top
        if player.rec.top < item.rec.bottom and player.rec.bottom > item.rec.bottom:
            player.rec.top = item.rec.bottom