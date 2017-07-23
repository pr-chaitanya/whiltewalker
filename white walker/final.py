# 1 - Import library
import pygame
import time
import random
from pygame.locals import *
 
# 2 - Initialize the game
pygame.init()
width, height = 1200, 600
white=(255,255,255)
grey=(100,100,100)
black=(0,0,0)
blue=(0,0,200)
darkblue=(0,0,255)
red=(255,0,0)
green=(0,155,0)
ka=1
kb=0
kc=0  
x=60
y=250
l5=0
l10=0
nbkey15=0
nbkey10=0
life=100
disp1=0
disp2=1200
bdx=0
dy=0
s=0
dx=0
mw=75
mh=100
hba=random.randrange(1,3)*100
hbb=random.randrange(0,3)*100
hbc=random.randrange(0,3)*100
hbd=random.randrange(0,3)*100
f=0
lpy=480
score=0
move=0
nb=0
wa=400
wb=400
wc=400
wd=400
i=0
t=1
bxaa=1200
bxbb=bxaa+wa
bxcc=bxbb+wb
bxdd=bxcc+wc
time=0
clock=pygame.time.Clock()
screen=pygame.display.set_mode((width, height))
# pygame.display.set_caption('Game')
# 3 - Load images 
man1 = pygame.image.load('1.png')
fman = pygame.image.load('1.png')
man2 = pygame.image.load('2.png')
man3 = pygame.image.load('3.png')
man4 = pygame.image.load('4.png')
man5= pygame.image.load('5.png')
man6= pygame.image.load('6.png')
plus= pygame.image.load('+.jpg')

#man2 = pygame.image.load('C:/Users/Mandy/Desktop/imgs2.png')
img=pygame.image.load('bg.jpg')
#img1=pygame.image.load('C:/Users/Mandy/Desktop/pic1.png')
img2=pygame.image.load('bottom.png')
fire=pygame.image.load('fire.png')
plus=pygame.image.load('+.jpg')
font=pygame.font.SysFont(None,40)
sfont=pygame.font.SysFont(None,30)
# 4 - keep looping through
while 1:
    i=i+1
    if x<400:
        t=1
    else :
        t=0
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        print(event)
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)   
        if event.type == KEYDOWN:
            if event.key == K_UP :
                 dy=dy-20
                 f=1
            elif event.key == K_DOWN:
                dy=dy+20
            elif event.key == K_LEFT:
                dx=dx-20
                s=0
            elif  event.key == K_RIGHT:
                
                move=1
                s=1
        elif event.type == KEYUP:
            if event.key == K_UP:
                 dy=0
                 y=lpy
                 f=0
                 
            elif event.key == K_DOWN:
                dy=0
            elif event.key == K_LEFT:
                dx=0
            elif event.key == K_RIGHT:
                bdx=0
                move=0
                s=0
                dx=0
    if y<0: f=0;           
    if s==1 and t==1 :
        dx=8
    if t==0 and s==1 :
        dx=0
    if s==1 and t==0:
       bdx=-20
       disp1=disp1-7
       disp2=disp2-7
    
    if(f==0): y=lpy
    '''if(y+200>=450 and f==0):
        dy=0
        y=250
    if(y<=0): dy=10
    '''    
    x=x+dx
    y=y+dy
    
    # 5 - clear the screen before drawing it again
    screen.fill(white)
    # 6 - draw the screen elements
    
    #screen.blit(img,(disp1,0))
    #screen.blit(img,(disp2,0))

    if t==1:
        bdx=0
    bxaa= bxaa+bdx
    bxbb= bxbb+bdx
    bxcc= bxcc+bdx
    bxdd= bxdd+bdx
    if nb%9==1 and nbkey15==0:
        l5=1        
    if l5==1:
          screen.fill(red,[bxaa+100,580-hba-30,30,30])
    if nb%11==1 and nbkey10==0:
        l10=1        
    if l10==1:
          #screen.fill(green,[bxcc+100,580-hbc-200,30,30])
          screen.blit(plus,(bxcc+100,580-hbc-200))
          
    if(life>30):
        screen.fill(green,[350,47,life,20])      
    else:
        screen.fill(red,[400,50,life,20])      
    '''screen.fill(black,[bxaa,450-hba,350,hba])
    screen.fill(grey,[bxbb,450-hbb,wb,hbb])
    screen.fill(green,[bxcc,450-hbc,wc,hbc])
    screen.fill(blue,[bxdd,450-hbd,wd,hbd])'''
    screen.blit(fire,(bxaa,580-hba))
    screen.blit(fire,(bxbb,580-hbb))
    screen.blit(fire,(bxcc,580-hbc))
    screen.blit(fire,(bxdd,580-hbd))
    screen.blit(img2,(0,580))
    if(f>0):
        screen.blit(fman, (x,y))
    else :
        if move==1:
            if i%6==1:
                screen.blit(man1, (x,y)) 
            elif i%6==2 :
                screen.blit(man2, (x,y))
            elif i%6==3 :
                screen.blit(man3, (x,y))
            elif i%6==4 :
                screen.blit(man4, (x,y))
            elif i%6==5 :
                screen.blit(man5, (x,y))
            elif i%6==0 :
                screen.blit(man6, (x,y))
        else:
            screen.blit(man1,(x,y)) 
    screentext=sfont.render("Score: "+str(score)+"                        Life: "+str(life),True,blue)
    screen.blit(screentext,(20,50))
    def messagetoscreen(msg,color):
          screentext=font.render(msg,True,color)
          screen.blit(screentext,[300,100])

    # 7 - update the screen
    pygame.display.update()
    clock.tick(25)
    if(nbkey15==0 and l5==1 and bxaa+115<x+mw and x<bxaa+115 and y+mh>580-hba-30):
      life-=15      
      l5=0
      nbkey15=1
    if(nbkey10==0 and l10==1 and bxcc+115<x+mw and x<bxcc+115 and y+mh>580-hbc-200 and y<580-hbc-200):
      life+=10      
      l10=0
      nbkey10=1
    if(x+mw >= bxaa and ka==1 ):    
      kb=1
      if(y+mh > 580-hba):
               #score-=1
               life-=1
               messagetoscreen("You hit a",red)        
               pygame.display.update()
      elif(y+mh <= 580-hba and hba>=hbd):           
                   lpy=580-mh-hba
                   kd=0
      elif(y+mh <= 580-hbd and hba<hbd and x >= bxdd+wd):           
                   lpy=580-mh-hba
                   kd=0       
      elif(x >= bxdd+wd):     
                   lpy=580-mh-hba
                   kd=0
                 
    
    if(x+mw >= bxbb and kb==1 ):    
      kc=1
      if(y+mh > 580-hbb):
               #score-=1
               life-=1
               messagetoscreen("You hit b",red)        
               pygame.display.update()
               
      elif(y+mh <= 580-hbb and hbb>=hba):           
               lpy=580-mh-hbb
               ka=0
      elif(y+mh <= 580-hbc and hbb<hba and x >= bxaa+wa):           
               lpy=580-mh-hbb
               ka=0
      elif(x >= bxaa+wa):     
               lpy=580-mh-hbb
               ka=0
             
     
    if(x+mw >= bxcc and kc==1 ):    
      kd=1
      if(y+mh > 580-hbc):
               #score-=1
               life-=1
               messagetoscreen("You hit c",red)        
               pygame.display.update()
               
      elif(y+mh <= 580-hbc and hbc>=hbb):           
               lpy=580-mh-hbc
               kb=0
      elif(y+mh <= 580-hbc and hbc<hbb and x >= bxbb+wb):           
               lpy=580-mh-hbc
               kb=0
      elif(x >= bxbb+wb):     
               lpy=580-mh-hbc
               kb=0  
               
    if(x+mw >= bxdd and kd==1 ):    
      ka=1
      if(y+mh > 580-hbd):
               #score-=1
               life-=1
               messagetoscreen("You hit d",red)        
               pygame.display.update()
               
      elif(y+mh <= 580-hbd and hbd>=hbc):           
               lpy=580-mh-hbd
               kc=0
      elif(y+mh <= 580-hbd and hbd<hbc and x >= bxcc+wc):           
               lpy=580-mh-hbd
               kc=0
      elif(x >= bxdd+wd):     
               lpy=580-mh-hbd
               kc=0          
         
    if(bxaa+400<0):
        bxaa=1200
        score+=10
        hba=random.randrange(0,3)*100
        nb+=1
        nbkey15=0
        nbkey10=0
    if(bxbb+wb<0):
        score+=10
        nb+=1
        bxbb=1200
        hbb=random.randrange(0,3)*100
        nbkey15=0
        nbkey10=0
    if(bxcc+wc<0):
        nb+=1
        score+=10
        hbc=random.randrange(0,3)*100   
        bxcc=1200
        nbkey15=0
        nbkey10=0
    if(bxdd+wd<0):
        nb+=1
        score+=10
        nbkey=0
        hbd=random.randrange(0,3)*100   
        bxdd=1200
        nbkey10=0
        nbkey15=0
    if(bxaa+400<=0 and l5==1):
        l5=0
    if disp1+1200<0:
         disp1=1200

    if disp2+1200<0:
         disp2=1200
