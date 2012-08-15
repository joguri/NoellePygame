import pygame, sys, item, itemlist, collision

pygame.init()
#set constants
SPEED = 10

#Create the screen
screen = pygame.display.set_mode((800,600))

#Add all the items: background, character, platforms, enemies, etc
background = item.Item("Background.png")
player = item.Character("Birdy.png")
platform = item.Item("Platform.png")
platform.rec.move_ip(200,200)
platform2 = item.Item("Platform.png")
platform2.rec.move_ip (470, 200)
platform3 = item.Item("Platform.png")
platform3.rec.move_ip(0,150)

#create a list of all the items. Add the items to the list, then put them on the screen
myList = itemlist.Itemlist()
myList.addBackground(background)
myList.addCharacter(player)
myList.addPlatform(platform)
myList.addPlatform(platform2)
myList.addPlatform(platform3)
myList.redraw(screen)

#Now we wait for events
while(1==1):
    player.movex()
    collision.snapHorizontal(player, myList.platformList)
    player.movey()
    collision.snapVertical(player, myList.platformList)       
    myList.redraw(screen)
    
    if collision.inAir(player, myList.platformList):
        if player.vSpeed < 16:
            player.vSpeed = player.vSpeed + 1
    else:
        player.vSpeed = 0
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.hSpeed = player.hSpeed + SPEED
            elif event.key == pygame.K_LEFT:
                player.hSpeed = player.hSpeed - SPEED
            elif event.key == pygame.K_UP:
                player.vSpeed = player.vSpeed - SPEED
            elif event.key == pygame.K_DOWN:
                player.vSpeed = player.vSpeed + SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.hSpeed = player.hSpeed - SPEED
            elif event.key == pygame.K_LEFT:
                player.hSpeed = player.hSpeed + SPEED
            elif event.key == pygame.K_UP:
                player.vSpeed = player.vSpeed + SPEED
            elif event.key == pygame.K_DOWN:
                player.vSpeed = player.vSpeed - SPEED
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(10)
