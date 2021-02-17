import functions
import FormMain as main
import pygame
false = False
true = True
screen=functions.set_screen((800,600),"Main Window","images\\icon.png",True,True)
running = true
while running:
    running =main.run(screen)
quit()
