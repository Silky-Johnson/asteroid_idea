import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField() 

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        for sprite in updatable:
            sprite.update(dt)
       
       
        for asteroid in asteroid_group:
            if asteroid.collision(player):
                print("Game Over!")
                exit()
            
            for bullet in bullets:
                if bullet.collision(asteroid):
                    asteroid.split()
                    bullet.kill()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
 
        dt = fps.tick(60) / 1000
        

if __name__ == "__main__":
    main()
