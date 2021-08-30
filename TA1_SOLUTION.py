import pygame
import random
#Import time module
import time

pygame.init()

class Player:
  def __init__(self,name,image,x,y):
    self.name=name
    self.image=image
    self.num=num
    self.x=x
    self.y=y

  def location_update(self,event):
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_UP:
          self.y-=10
      if event.key==pygame.K_DOWN:
          self.y+=10
      if event.key==pygame.K_LEFT:
          self.x-=10
      if event.key==pygame.K_RIGHT:
          self.y+=10
  
  def time_update(self,time):
    self.gametime=time
          
def image_load(location,length,width):
    img=pygame.image.load(location).convert_alpha()
    img_scaled=pygame.transform.smoothscale(img,(length,width))
    return img_scaled
def text_display(size,text,r,g,b,x,y):
    font = pygame.font.Font(None, size)
    text = font.render(text, 1, (r,g,b))
    screen.blit(text, (x,y))
#Create function here
def obs_location():
  x_choice=[150,200,250]
  x=random.choice(x_choice)
  y=random.randint(0,cary-200)
  return(x,y)



size = (350, 400)
screen = pygame.display.set_mode(size)
carx=60
cary=340
#Create variables
car2x=130
car2y=200
threshold=0
roadx=-10
roady=0
threshold=0
#Create a counter variable
counter=0


#Replace file location address on your computer
road=image_load("Assets/road.png",400,800)

#Replace file location address on your computer
car=image_load("Assets/yellowCar.png",70,60)

#Replace file location address on your computer
stone=image_load("Assets/stone.png",70,60)

#create player object here 
player_count=firebase.get("","player_count")
if player_count<=3:
  player_count+=1
  player_count=firebase.put("","player_count",player_count)
  player=Player("John",player_count,150,200)

if player_count==3:
  print("LOBBY FULL")
  pygame.time.wait(2000)
  pygame.quit()



carryOn = True

#Create timepoint t1 here
t1=time.time()

x,y=obs_location()
while carryOn:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False
  
  screen.blit(road,(roadx,roady))
  screen.blit(car,(carx,cary))
  #screen.blit(car2,(car2x,car2y))
  
 #update location here 
  player1.location_update(event)





  if cary<=0:
    #Increment counter by 1
    counter+=1
    roady=0
    cary=340
    x,y=obs_location
  car_rect=car.get_rect(topleft=(carx,cary))
  stone_rect=stone.get_rect(topleft=(x,y))
  

  if car_rect.collidepoint(stone_rect.x,stone_rect.y):
    cary=360
  
  
  screen.blit(stone,[x,y])
  #Create second time point here
  t2=time.time()
  #Evaluate gametime here
  game_time=t2-t1
  game_time=round(game_time,2)
  #update game time here
  player1.time_update(game_time)
  
  #Display gametime here
  text_display(24,"TIME ELAPSED: " + str(game_time)+"seconds",255,0,255,50,10)

  #Display distance
  distance=counter*6
  font = pygame.font.Font(None, 24)
  text = font.render("DISTANCE: " + str(distance)+"km", 1,(255,255,0))
  screen.blit(text, (50,30))



  #Check if Key is pressed
  if event.type==pygame.KEYDOWN:
  #Check if key pressed is "Enter"
        if event.key==pygame.K_RETURN:
        #Check if game time is within threshold
            if game_time>=threshold and game_time<=(threshold+10):
                    #Decrement "cary" to make car move forward
                    cary-=10 
                    #Increment "threshold" by 10
                    threshold+=10
  
  
  #check if counter is equal to 100
  if counter>=5:
    #Create the finish line rectangle
    finishline=pygame.Rect(50,40,240,20)
    #Draw the rectangle
    pygame.draw.rect(screen,(255,255,255),finishline)
    font = pygame.font.Font(None, 20)
    text = font.render("FINISH", 1,(255,0,0))
    screen.blit(text, (150,40))

  if counter>=5 and cary<=50:
    pygame.time.wait(2000)
    screen.fill((0,100,255))
    font = pygame.font.Font(None, 34)
    text = font.render("Finish time:"+str(round(game_time,2))+"seconds", 1,(255,100,0))
    screen.blit(text, (50,200))
    pygame.display.flip()
    pygame.time.wait(2000)
    break
  
  
  
  pygame.display.flip()
  
pygame.quit()
