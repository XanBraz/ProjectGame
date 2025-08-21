import pygame

print('Setup Star')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Star')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit() # close window
            quit() # end pygame
