import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400,1))

stopwatch = 0

sound = pygame.mixer.Sound("images/record.wav")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.Sound.play(sound)
    stopwatch += 1
    if (stopwatch / 500) % 1 == 0:
        pygame.mixer.Sound.play(sound)
    pygame.display.flip()
