import pygame
pygame.mixer.init()
pygame.mixer.music.load("teq.mp3")
pygame.mixer.music.play()
print("h")
while pygame.mixer.music.get_busy() == True:
    continue