import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scoreboard import Scoreboard

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asters = pygame.sprite.Group()
shots = pygame.sprite.Group()
scores = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asters)
AsteroidField.containers = (updatable,)
Shot.containers = (updatable, drawable, shots)
Scoreboard.containers = (updatable, drawable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    trackscore = Scoreboard()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for ast in asters:
            if ast.collide(player):
                print("Game over!")
                print(f"Score: {trackscore.score}")
                sys.exit()

            for bullet in shots:
                if bullet.collide(ast):
                    bullet.kill()
                    ast.split()
                    trackscore.add_points(ast.get_points())
                    

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        trackscore.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()


