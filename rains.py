import pygame
from pygame.sprite import Sprite
class Rains(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.rndp=pygame.image.load("D:/myProjects/rain_drop/new_rain.bmp")
        self.image=pygame.transform.scale(self.rndp,(50,50))
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    def update_rain(self):
        self.y += 0.01  # Move the raindrop down

    # If the raindrop has moved past the screen height, reset its position to the top
        if self.rect.top > self.screen.get_height():
            self.y = -self.rect.height  # Reset y to just above the screen to start falling again

        self.rect.y = self.y  # Update the rect position

"""   def update_rain(self):
        self.y+=0.5
        
        self.rect.y=self.y
"""