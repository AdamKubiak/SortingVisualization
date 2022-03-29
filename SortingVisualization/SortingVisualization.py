import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800,800

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sorting Vis")

WHITE = (255,255,255)
GREY = (200,200,200)


class Bar:
    amount = 800
    barList = []
    def __init__(self,width,value):
        self.width = width
        self.hight = value
        #dodać indeks paska żeby pozbyć się i = 0 z maina



    def draw(self,win,grey_scale,position_x):
        pygame.draw.rect(win,grey_scale,pygame.Rect(position_x,WIDTH-self.hight,self.width,self.hight))


    def generateSet():
        for i in range(Bar.amount):
            Bar.barList.append(Bar(WIDTH/Bar.amount,random.randrange(70,700)))


def main():
    run = True
    clock = pygame.time.Clock()
    #bar = Bar(4,730)
    Bar.generateSet()
    print(Bar.barList)
    
   
    while(run):
        clock.tick(5)
        WIN.fill(WHITE)
        i = 0
        for bar in Bar.barList:
            bar.draw(WIN,GREY,i)
            i+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #bar.draw(WIN,GREY,400)
        
        pygame.display.flip()
    
    pygame.quit()


main()

      
