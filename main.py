import pygame
import os

#set up display

pygame.init() #initializing pygames
WIDTH, HEIGHT = 800, 500 #constants represented in all caps
win = pygame.display.set_mode((WIDTH, HEIGHT)) #pygame accepts a tuple for width and height
pygame.display.set_caption("Hangman Game!") #sets the caption (label on top)

#button variables
RADIUS = 20
GAP = 15
LETTERS = []
startx = round((WIDTH - (RADIUS * 2 + GAP)*13)/2 )
starty = 400
for i in range(26): #i tells which button we are on 
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
  y = starty + ((i // 13) * (GAP + RADIUS * 2)) # // = integer division, just excludes the division point 
  

#load images 
images = []
for i in range(7): 
  image = pygame.image.load("hangman" + str(i) + ".png")
  images.append(image)

#game variables
hangman_status = 4


#colors
WHITE = (255,255,255)

#set game loop

FPS = 60 #frames per second
clock = pygame.time.Clock() #clock object that counts at 60 FPS 
run = True

while (run):
  clock.tick(FPS) #ticks the clock at 60 FPS
  win.fill(WHITE)
  win.blit(images[hangman_status], (150, 100)) #stands for draw image & the POS of the image
  pygame.display.update() #need to update the display to see the changes
  
  for event in pygame.event.get(): #look for any event that happens ex. user clicking the screen with their mouse
    if event.type == pygame.QUIT: #if the user clicks the X on the window
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      print(pos) #(0,0) coordinate is at the top left of the screen

pygame.quit()