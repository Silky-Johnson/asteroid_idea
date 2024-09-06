import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    updatable = []
    drawable = []
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
        #if self.position.x <= 0 or self.position.x >= SCREEN_WIDTH:
        #    print("We have went out of bounds")
        #elif self.position.y <= 0 or self.position.y >= SCREEN_HEIGHT:
        #    print("Y has been too far, out of bounds")

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)

        ast1.velocity = v1 * 1.2
        ast2.velocity = v2 * 1.2

