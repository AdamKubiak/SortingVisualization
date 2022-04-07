import pygame
import math
import random
import RandomNumberGenerator as rnd
#import MergeSort

def bubbleSort(arr,WIN):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j].hight > arr[j + 1].hight :
                arr[j].hight, arr[j + 1].hight = arr[j + 1].hight, arr[j].hight
                drawALL(WIN)
                #yield True
                
pygame.init()

WIDTH, HEIGHT = 800,800

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sorting Vis")

WHITE = (255,255,255)
GREY = (200,200,200)


class Bar:
    amount = 200
    barList = []
    color = [200,200,200]
    def __init__(self,width,value):
        self.width = width
        self.hight = value
        #dodać indeks paska żeby pozbyć się i = 0 z maina



    def draw(self,win,grey_scale,position_x):
        pygame.draw.rect(win,grey_scale,pygame.Rect(position_x, HEIGHT-self.hight,self.width,self.hight))


    def generateSet():
        y = rnd.RandomNumberGen.generate_numbers()
        for i in range(Bar.amount):
            Bar.barList.append(Bar(WIDTH/Bar.amount,y[i]))
   
    

def drawList():
        i=0
        for bar in Bar.barList:
            bar.draw(WIN,Bar.color,i)
            i+=1*WIDTH/Bar.amount

def drawALL(win):
    win.fill(WHITE)
    drawList()
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    Bar.generateSet()

    
    print("Given array is")
    #for i in range(n):
        #print(Bar.barList[i].hight,end=" ")
 
    #mergeSort(Bar.barList, 0, n-1)

    while(run):
        clock.tick(60)
        WIN.fill(WHITE)
        i = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #bar.draw(WIN,GREY,400)
        
        bubbleSort(Bar.barList,WIN)
        #pygame.display.flip()
    
    pygame.quit()


main()

      
