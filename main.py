import pygame

pygame.init()

infoObject = pygame.display.Info()
monitor_width = infoObject.current_w
monitor_height = infoObject.current_h

screen = pygame.display.set_mode((monitor_width, monitor_height))

goobCharacter = pygame.image.load('goob.png').convert_alpha()
goobCharacter = pygame.transform.scale(goobCharacter, (goobCharacter.get_width() * 3, goobCharacter.get_height() * 3))

goobX = screen.get_width()/2 - goobCharacter.get_width()/2
goobY = screen.get_height()/2 - goobCharacter.get_height()/2

running = True

clock = pygame.time.Clock()

while running:

    screen.blit(goobCharacter, (goobX, goobY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()




#to start venv code
#.\\venv\\Scripts\\activate.bat 
#python main.py