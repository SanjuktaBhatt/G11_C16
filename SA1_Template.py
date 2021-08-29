import pygame
import time
pygame.init() 

# Create image loading function here







#Create a function to display coins






size = (400, 400)
screen = pygame.display.set_mode(size)

#Load background image

#Load charachter image

#Load coin image
coin= image_load("Assets/coin.png",30,30)
#Create a list of 6 coins

#all variables required are defined here



carryOn = True
t1=time.time()
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False 
      
  #Move images according to user entry
  
  
  
      

  #display the background and charachter here
  
  
  #display the coins

 

  pygame.display.flip()
pygame.quit()
