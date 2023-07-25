#Notes:
    #The (0,0) coordinate is the top left not the centre

import pygame
import os #Helps in defining the path of images
from pygame.constants import QUIT
pygame.font.init()
pygame.init()

#Information about the window
width = 900
height = 500
wnd = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Fight')

#Fonts

Health_Font = pygame.font.SysFont('Helvatica', 40)
Winner_Font = pygame.font.SysFont('Helvatica', 100)


#Extra Events
FIRST_HIT = pygame.USEREVENT + 1 #This represents the code of a custom use event (used in the main function)
SECOND_HIT = pygame.USEREVENT + 2


#Colors used
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)


#Extra Information
BORDER = pygame.Rect(width//2 - 5, 0, 10, height)
FPS = 60
SPACESHIP_VEL = 5
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40
BULLET_VEL = 7
MAX_BULLETS = 5

#Images
first_spaceship_image = pygame.image.load(
    os.path.join('Assets', 'First_Spaceship.png')) #imports the spaceship img
first_spaceship = pygame.transform.rotate(pygame.transform.scale(
    first_spaceship_image,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)) , 90)
second_spaceship_image = pygame.image.load(
    os.path.join('Assets', 'Second_Spaceship.png')) #imports the spaceship img
second_spaceship = pygame.transform.rotate(pygame.transform.scale(
    second_spaceship_image,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

SPACE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'test4.jpg')), (width,height))


#Functions
def draw_window(first,second, first_bullets, second_bullets, first_health, second_health):
        '''This Function draws everything on the screen'''
        wnd.blit(SPACE_IMAGE, (0,0))
        pygame.draw.rect(wnd,black, BORDER)#(surface to be drwan on, color, rectangle to be drawn)
        first_health_text = Health_Font.render('First Player Lives: ' + str(first_health),1,white)
        second_health_text = Health_Font.render('Second Player Lives: ' + str(second_health),1,white)
        wnd.blit(first_health_text, (15,0))
        wnd.blit(second_health_text, (550,0))

        wnd.blit(first_spaceship, (first.x,first.y)) 
        wnd.blit(second_spaceship, (second.x,second.y))

        for bullet in first_bullets:
            pygame.draw.rect(wnd, yellow, bullet)
        for bullet in second_bullets:
            pygame.draw.rect(wnd, red, bullet)


        pygame.display.update() #Updates to the last thing that was drawn
def first_movement(keys_pressed,first):
        '''This function defines the controls and movement for the first spaceship'''
        if keys_pressed[pygame.K_a] and first.x - SPACESHIP_VEL > 0: #LEFT
            first.x -= SPACESHIP_VEL
        if keys_pressed[pygame.K_d] and first.x + SPACESHIP_VEL + first.width < BORDER.x: #Right
            first.x += SPACESHIP_VEL
        if keys_pressed[pygame.K_s] and first.y + SPACESHIP_VEL + first.height < height - 15 : #DOWN
            first.y += SPACESHIP_VEL
        if keys_pressed[pygame.K_w] and first.y - SPACESHIP_VEL > 0: #UP
            first.y -= SPACESHIP_VEL

def second_movement(keys_pressed,second):
        '''This function defines the controls and movement for the second spaceship'''
        if keys_pressed[pygame.K_LEFT] and second.x - SPACESHIP_VEL > BORDER.width + BORDER.x: #LEFT
            second.x -= SPACESHIP_VEL
        if keys_pressed[pygame.K_RIGHT] and second.x + SPACESHIP_VEL + second.width < width: #Right
            second.x += SPACESHIP_VEL
        if keys_pressed[pygame.K_DOWN] and second.y + SPACESHIP_VEL + second.height < height - 15 : #DOWN
            second.y += SPACESHIP_VEL
        if keys_pressed[pygame.K_UP] and second.y - SPACESHIP_VEL > 0: #UP
            second.y -= SPACESHIP_VEL

def bullet_handling(first_bullets, second_bullets, first, second):
    '''THis function will move the bullets and handle their collision with the spaceships'''
    for bullet in first_bullets:
        bullet.x += BULLET_VEL
        if second.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SECOND_HIT)) #This is making a new event that is telling that the second player was hit
            first_bullets.remove(bullet)            
        elif bullet.x > width:
            first_bullets.remove(bullet)
    
    for bullet in second_bullets:
        bullet.x -= BULLET_VEL
        if first.colliderect(bullet):
            pygame.event.post(pygame.event.Event(FIRST_HIT)) #This is making a new event that is telling that the first player was hit
            second_bullets.remove(bullet)
        elif bullet.x < 0:
            second_bullets.remove(bullet)

def draw_winner(text):
    '''This Function Pops Up The winner's message'''
    draw_text = Winner_Font.render(text,1,white)
    wnd.blit(draw_text, (width/2 - draw_text.get_width() /
                         2, height/2 - draw_text.get_height()/2))   
    pygame.display.update()
    pygame.time.delay(3000) #




def main():
    '''This is the main functions which contains the game's main loop'''
    first = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    first_bullets = []
    first_health = 10

    second = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    second_bullets = []
    second_health = 10

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS) # Makes sure that the frames per second is 60 
        #Checking for events in the game
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN: #Checks if a key has been pressed
                if event.key == pygame.K_LCTRL and len(first_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(first.x + first.width, first.y + first.height//2 - 2, 10 ,5)
                    first_bullets.append(bullet)


                if event.key == pygame.K_RCTRL and len(second_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(second.x , second.y + second.height//2 - 2, 10 ,5)
                    second_bullets.append(bullet)
            if event.type == FIRST_HIT:
                first_health -= 1
            
            if event.type == SECOND_HIT:
                second_health -= 1
        #Creating Winner text
        winner_text = ''
        if first_health == 0:
            winner_text = 'Second Player Wins'

        if second_health == 0:
            winner_text = 'First Player Wins'

        if winner_text != '':
            draw_winner(winner_text)
            break
        
        #Calling all the functions
        keys_pressed = pygame.key.get_pressed()
        first_movement(keys_pressed,first)
        second_movement(keys_pressed,second)
        bullet_handling(first_bullets,second_bullets,first,second)
        draw_window(first,second,first_bullets,second_bullets, first_health, second_health)

    main()
if __name__ == "__main__": #Makes sure that the file is opened only when it is opened directly, not when imported
    main()