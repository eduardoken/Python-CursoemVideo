# Faça um programa em python que abra e reproduza um audio de um arquivo mp3.
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
