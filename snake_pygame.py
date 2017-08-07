# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 17:12:43 2016

@author: Dallas Nowak

"""

import pygame
import time
import random

pygame.init() # initializes pygame

#initializing colors to be used 
white = (255,255,255)

black = (0,0,0)

red = (255,0,0)

green = (0,155,0)

# setting window size
display_width = 800

display_height = 600

game_display = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Snake")

icon = pygame.image.load("snake_icon.png")
pygame.display.set_icon(icon)




block_size = 20 # size of snake

apple_thickness = 20


fps = 15 # Speed that the game updates at 

clock = pygame.time.Clock()

#initializing fonts 
small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 50)
large_font = pygame.font.SysFont("comicsansms", 75)

""" Displays start menu where user can either play or quit """
def start_menu():
    start = True
    
    game_display.fill(white)
    message_to_screen("Welcome to Snake",green,-30,"large")
    message_to_screen("Classic snake game: eat the apples",black,10)
    message_to_screen("The game is over if you run into yourself or the edges!",black,50)
    message_to_screen("Press P to Play or Q to Quit!",black,80)
        
    pygame.display.update()
    while start:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    start = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


# Draws snake to screen					
def snake(block_size,snakelist):
    for coordinates in snakelist:
        pygame.draw.rect(game_display,green,[coordinates[0],coordinates[1],block_size,block_size])
    
# Returns a text object based on color and size
def text_objects(text,color, size):
    if (size == "small"):
        textSurface = small_font.render(text,True,color)
    elif (size == "medium"):
        textSurface = med_font.render(text,True,color)
        
    elif (size == "large"):
        textSurface = large_font.render(text,True,color)
    
    
    return textSurface, textSurface.get_rect()
    

# Prints message
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    game_display.blit(textSurf,textRect)

# Occurs after start menu until user quits	
def game_loop():
    game_exit = False
    game_over = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0 
    
    snake_list = []
    
    snake_length = 1
    
    rand_apple_x = round(random.randrange(0,display_width-block_size))#/10.0) * 10.0
    rand_apple_y = round(random.randrange(0,display_height-block_size))#/10.0) * 10.0
    
    while not game_exit:
        
        while game_over == True:
            game_display.fill(white)
            message_to_screen("Game over!",red,-50, size = "large")
            message_to_screen("Press P to play again; Q to quit", black, 50)
            pygame.display.update()
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                        
                    if event.key == pygame.K_p:
                        game_loop()
        
        
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    
                
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size    
                    lead_x_change = 0
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True
        
            
                
        lead_x += lead_x_change
        lead_y += lead_y_change          
        
        game_display.fill(white)
        
        
        pygame.draw.rect(game_display,red,[rand_apple_x,rand_apple_y,apple_thickness,apple_thickness])
        
        
        
        snake_head = []
        
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for segment in snake_list[:-1]: # Analyze anything but snake head:
            if segment == snake_list[-1]:
                game_over = True
            
        
        snake(block_size,snake_list)
        
        the_score = snake_length - 1  
        
        message_to_screen("Score: " + str(the_score),black)
        
        
        
        pygame.display.update()
        
        
#        
        
        # Crossover logic
        
        if lead_x > rand_apple_x and lead_x < (rand_apple_x + apple_thickness) or (lead_x + block_size > rand_apple_x and lead_x + block_size < rand_apple_x + apple_thickness):
            
            
            if lead_y > rand_apple_y and lead_y < (rand_apple_y + apple_thickness):
                
                
                rand_apple_x = round(random.randrange(0,display_width-apple_thickness))#/10.0) * 10.0
                rand_apple_y = round(random.randrange(0,display_height-apple_thickness))#/10.0) * 10.0
                snake_length += 1
                
            elif lead_y + block_size > rand_apple_y and lead_y + block_size < rand_apple_y + apple_thickness:
                
                
                rand_apple_x = round(random.randrange(0,display_width-apple_thickness))#/10.0) * 10.0
                rand_apple_y = round(random.randrange(0,display_height-apple_thickness))#/10.0) * 10.0
                snake_length += 1
            
        
        clock.tick(fps)
    
    
    
    pygame.quit()
    
    quit()
start_menu()    
game_loop()