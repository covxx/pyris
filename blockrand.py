#Importing and initiating
import pygame,sys,random,time
from pygame.locals import *
from random import randint
pygame.init()

#Screen Display
window = pygame.display.set_mode((550, 600),0,32)

#Importing block images
colors = ["red.jpg","blue.jpg","purple.jpg","pink.jpg","yellow.jpg","green.jpg"]
blocks = []

for x in colors:
    tetblock = "data/images/" + x
    blocks.append(tetblock)
    
block_images = []
for x in blocks:
    block_image=pygame.image.load(x).convert()
    block_images.append(block_image)
pointx=12.5
pointy=12.5
flag=0
##print block_images
####
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    choice = randint(0,5)
    print colors[choice]
    bchoice = block_images[choice]
    print bchoice
    while flag == 0:
        for x in range (0,4):
            window.blit(bchoice, bchoice.get_rect(center=(pointx,pointy)))
            if pointx < 62.5:
                pointx+=25
            elif pointx == 62.5:
                pointy+=25
            flag+=1
##    if event .type == KEYDOWN:
##        if event.key == K_RIGHT:
    pygame.display.update()
    time.sleep(2)
