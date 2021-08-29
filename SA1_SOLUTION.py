import pygame
import time
pygame.init() 

# Create image loading function here
def image_load(location,length,width):
    img=pygame.image.load(location).convert_alpha()
    img_scaled=pygame.transform.smoothscale(img,(length,width))
    return img_scaled
def coin_display():
  x=0
  for i in coins:
    screen.blit(i,(50*(x+1)+50,240))
    x+=1
 #Collection function   


size = (400, 400)
screen = pygame.display.set_mode(size)
bg=image_load("Assets/bg.png",800,400)
char=image_load("Assets/character.png",40,60)
coin= image_load("Assets/coin.png",30,30)
coins=[coin for i in range(6)]
#all variables required are defined here
bgx=0
charx,chary=10,240
money=0
total_time=300


carryOn = True

while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False  
  if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_RIGHT:
      charx+=1
      bgx-=1
  if charx>=350:
    charx=10
    bgx=0
    coins=[coin for i in range(6)]
    
    
  #display the background and charaacter here
  screen.blit(bg,(bgx,0))
  screen.blit(char,(charx,chary))
  coin_display()

 

  pygame.display.flip()
pygame.quit()
