import pygame
import constants
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = updatable, drawable

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    dt = 0

    print ("Starting asteroids!")
    print (f"Screen width: {constants.SCREEN_WIDTH}")  
    print (f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        dt = clock.tick(60) / 1000 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
 
if __name__ == "__main__":
    main()  
