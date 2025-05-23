import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.font = pygame.font.SysFont(None, 40)

    def add_points(self, points):
        self.score += points
            
    def draw(self, screen):
        score_surface = self.font.render(f"Score: {self.score}", True, (0, 255, 0))
        x = 10
        y = SCREEN_HEIGHT - score_surface.get_height() -10
        screen.blit(score_surface, (x, y,))
    
    def update(self, dt):
        pass
    